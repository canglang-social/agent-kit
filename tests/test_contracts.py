import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT / "plugins" / "core"
SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")


def read(path: str | Path) -> str:
    target = path if isinstance(path, Path) else ROOT / path
    return target.read_text(encoding="utf-8")


def load_json(path: str | Path) -> dict:
    return json.loads(read(path))


def frontmatter(path: str | Path) -> dict[str, str]:
    text = read(path)
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if match is None:
        raise AssertionError(f"missing frontmatter: {path}")
    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        key, separator, value = line.partition(":")
        if separator:
            values[key.strip()] = value.strip()
    return values


class JsonAndManifestTests(unittest.TestCase):
    def test_every_tracked_json_parses(self) -> None:
        json_paths = sorted(ROOT.glob("**/*.json"))
        self.assertGreaterEqual(len(json_paths), 5)
        for path in json_paths:
            with self.subTest(path=path.relative_to(ROOT)):
                self.assertIsInstance(load_json(path), dict)

    def test_codex_marketplace_points_to_core_with_policy(self) -> None:
        marketplace = load_json(".agents/plugins/marketplace.json")
        self.assertEqual(marketplace["name"], "agent-kit")
        self.assertEqual(len(marketplace["plugins"]), 1)
        entry = marketplace["plugins"][0]
        self.assertEqual(entry["name"], "core")
        self.assertEqual(
            entry["source"], {"source": "local", "path": "./plugins/core"}
        )
        self.assertEqual(entry["policy"]["installation"], "AVAILABLE")
        self.assertEqual(entry["policy"]["authentication"], "ON_INSTALL")
        self.assertEqual(entry["category"], "Productivity")

    def test_claude_marketplace_still_points_to_core(self) -> None:
        marketplace = load_json(".claude-plugin/marketplace.json")
        self.assertEqual(marketplace["name"], "agent-kit")
        self.assertEqual(marketplace["plugins"][0]["source"], "./plugins/core")

    def test_core_manifest_versions_are_strict_and_lockstep(self) -> None:
        claude = load_json(CORE / ".claude-plugin" / "plugin.json")
        codex = load_json(CORE / ".codex-plugin" / "plugin.json")
        self.assertEqual(claude["name"], CORE.name)
        self.assertEqual(codex["name"], CORE.name)
        self.assertEqual(claude["version"], codex["version"])
        self.assertEqual(codex["version"], "0.7.0")
        self.assertRegex(codex["version"], SEMVER)
        self.assertEqual(codex["skills"], "./codex/skills/")
        for unsupported in ("hooks", "mcpServers", "apps"):
            self.assertNotIn(unsupported, codex)


class SkillContractTests(unittest.TestCase):
    def test_shared_skill_catalog_has_exactly_two_bodies(self) -> None:
        skills = sorted((CORE / "skills").glob("*/SKILL.md"))
        self.assertEqual([path.parent.name for path in skills], ["learn", "prompt-engineer"])

    def test_codex_explain_is_isolated_and_fail_closed(self) -> None:
        codex_skills = sorted((CORE / "codex" / "skills").glob("*/SKILL.md"))
        self.assertEqual(
            [path.parent.name for path in codex_skills],
            ["explain", "learn", "prompt-engineer"],
        )
        explain_path = CORE / "codex" / "skills" / "explain" / "SKILL.md"
        adapter = read(explain_path)
        metadata = frontmatter(explain_path)
        self.assertEqual(set(metadata), {"name", "description"})
        self.assertEqual(metadata["name"], "explain")
        self.assertIn("../../../capabilities/explain.md", adapter)
        self.assertIn("missing or unreadable", adapter)
        self.assertIn("Never reconstruct it from memory", " ".join(adapter.split()))
        self.assertIn("read-only", adapter)
        self.assertIn("`$core:learn`", adapter)
        self.assertNotIn("Label every explanatory claim", adapter)
        self.assertTrue(
            (explain_path.parent / "agents" / "openai.yaml").is_file()
        )

    def test_codex_shared_skill_loaders_are_thin_and_fail_closed(self) -> None:
        cases = {
            "learn": ("../../../skills/learn/SKILL.md", "0.6.0", "Phase 4"),
            "prompt-engineer": (
                "../../../skills/prompt-engineer/SKILL.md",
                "0.3.0",
                "## How to build the prompt",
            ),
        }
        for name, (canonical_path, version, duplicated_heading) in cases.items():
            with self.subTest(skill=name):
                loader_path = CORE / "codex" / "skills" / name / "SKILL.md"
                loader = read(loader_path)
                self.assertEqual(frontmatter(loader_path)["name"], name)
                self.assertIn(canonical_path, loader)
                self.assertIn("missing or unreadable", loader)
                self.assertIn("Never reconstruct it from memory", " ".join(loader.split()))
                self.assertNotIn(duplicated_heading, loader)
                self.assertLess(len(loader.splitlines()), 25)
                self.assertEqual(
                    frontmatter(CORE / "skills" / name / "SKILL.md")["version"],
                    version,
                )
                ui = read(loader_path.parent / "agents" / "openai.yaml")
                self.assertIn(f"$core:{name}", ui)

    def test_explain_adapters_mirror_canonical_version_and_boundaries(self) -> None:
        canonical = frontmatter(CORE / "capabilities" / "explain.md")
        claude = frontmatter(CORE / "agents" / "explain.md")
        self.assertEqual(claude["version"], canonical["version"])
        canonical_text = read(CORE / "capabilities" / "explain.md")
        self.assertIn("single response", canonical_text)
        self.assertIn("zero writes", canonical_text)
        self.assertIn("Do not discover profiles", canonical_text)

    def test_learn_binds_current_invocation_and_fails_closed(self) -> None:
        learn = read(CORE / "skills" / "learn" / "SKILL.md")
        self.assertIn("Bind `TOPIC` from the current invocation", learn)
        self.assertIn("Never treat the literal text `$ARGUMENTS`", learn)
        self.assertIn("exact path", learn)
        self.assertIn("ask once", learn)
        self.assertIn("fail closed", learn)
        self.assertIn("append", learn)
        self.assertIn("Selection gate", learn)
        self.assertIn("Review gate", learn)
        self.assertIn("Never write, edit, or refactor production code", learn)
        self.assertIn("allowed-tools:", learn)
        self.assertIn("sandbox and\n  approval prompts", learn)

    def test_prompt_engineer_uses_current_invocation_and_is_model_neutral(self) -> None:
        skill_path = CORE / "skills" / "prompt-engineer" / "SKILL.md"
        skill = read(skill_path)
        mirror = read("prompts/prompt-engineer.md")
        self.assertIn("Bind `ROUGH_IDEA` from the current invocation", skill)
        self.assertIn("remain model-neutral", skill)
        self.assertIn("remain model-neutral", mirror)
        self.assertEqual(frontmatter(skill_path)["version"], "0.3.0")
        self.assertEqual(frontmatter("prompts/prompt-engineer.md")["version"], "0.3.0")


class CatalogPrivacyAndHookTests(unittest.TestCase):
    def test_file_asset_catalog_is_complete(self) -> None:
        prompts = sorted(path.name for path in (ROOT / "prompts").glob("*.md"))
        snippets = sorted(path.name for path in (ROOT / "snippets").glob("*.md"))
        self.assertEqual(len(prompts), 6)
        self.assertEqual(
            snippets,
            ["about-me.example.md", "deployment-loaders.md", "prompt-preamble.md"],
        )
        readme = read("README.md")
        for name in prompts:
            self.assertIn(f"`prompts/{name}`", readme)
        for name in snippets:
            self.assertIn(f"`snippets/{name}`", readme)
        self.assertIn("`ask Codex to read <path> and follow it`", readme)
        self.assertIn("MCP: none", readme)

    def test_about_me_example_states_truth_without_private_payload(self) -> None:
        path = "snippets/about-me.example.md"
        text = read(path)
        self.assertEqual(frontmatter(path)["version"], "0.5.1")
        self.assertIn("Learn may use owner-supplied profile and vault data", text)
        self.assertIn("Explain uses only session-supplied background and language", text)
        self.assertNotIn("Learning skills (learn, explain) read this profile", text)
        self.assertNotRegex(text, r"/Users/[^<\s]+")

    def test_codex_hook_is_post_tool_use_and_non_mutating(self) -> None:
        hook = load_json(".codex/hooks.json")
        entries = hook["hooks"]["PostToolUse"]
        self.assertEqual(len(entries), 1)
        self.assertRegex(entries[0]["matcher"], r"apply_patch")
        command = entries[0]["hooks"][0]["command"]
        self.assertIn("systemMessage", command)
        for forbidden in (
            "plugin update",
            "plugin add",
            "marketplace update",
            "cachebuster",
            "sed -i",
            "git commit",
            "git push",
        ):
            self.assertNotIn(forbidden, command)

    def test_docs_do_not_claim_unsupported_runtime_parity(self) -> None:
        docs = "\n".join(read(path) for path in ("README.md", "AGENTS.md", "CLAUDE.md", "spec.md"))
        for unsupported_claim in (
            "Claude /plugin remains the sole",
            "full runtime parity",
            "identical permissions",
            "automatically activates raw prompts",
        ):
            self.assertNotIn(unsupported_claim, docs)
        self.assertIn("sandbox and approvals", " ".join(docs.split()))
        self.assertFalse((CORE / ".mcp.json").exists())


if __name__ == "__main__":
    unittest.main()
