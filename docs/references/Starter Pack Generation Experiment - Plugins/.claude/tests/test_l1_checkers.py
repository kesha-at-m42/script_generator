#!/usr/bin/env python3
"""
test_l1_checkers.py — Regression test suite for Layer 1 SP checkers.

Uses known Starter Pack files as golden inputs and verifies:
  1. Parser extracts expected interaction count, phase breakdown, patterns
  2. Each checker runs without error at each gate level
  3. Finding counts stay within expected ranges (not exact — SPs evolve)
  4. Specific known findings are present (regression guards)
  5. No false-positive regressions (known-good patterns not flagged)

Usage:
  python test_l1_checkers.py                    # run all tests
  python test_l1_checkers.py -v                 # verbose output
  python test_l1_checkers.py TestParser          # run only parser tests
  python test_l1_checkers.py TestInteraction     # run only interaction checker tests

Golden file: G3U2M7_Notion_Ready.md (most complete, Gate 4 PASS)
"""

import json
import os
import sys
import unittest

# Add scripts directory to path
SCRIPTS_DIR = os.path.join(os.path.dirname(__file__), '..', 'scripts')
sys.path.insert(0, os.path.abspath(SCRIPTS_DIR))

# Workspace root (where SP files live)
WORKSPACE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# Golden file
M7_FILE = os.path.join(WORKSPACE, 'G3U2M7_Notion_Ready.md')


def skip_if_no_golden_file(func):
    """Decorator to skip test if the golden file doesn't exist."""
    def wrapper(*args, **kwargs):
        if not os.path.exists(M7_FILE):
            raise unittest.SkipTest(f"Golden file not found: {M7_FILE}")
        return func(*args, **kwargs)
    return wrapper


# ---------------------------------------------------------------------------
# Test: Parser (sp_parse_interactions.py)
# ---------------------------------------------------------------------------

class TestParser(unittest.TestCase):
    """Verify the shared parser produces correct structural output."""

    @classmethod
    def setUpClass(cls):
        if not os.path.exists(M7_FILE):
            raise unittest.SkipTest("Golden file not found")
        from sp_parse_interactions import parse_sp, filter_by_gate
        cls.sp = parse_sp(M7_FILE)
        cls.sp_g4 = filter_by_gate(cls.sp, 4)

    def test_interaction_count(self):
        """M7 should have ~28 interactions at Gate 4."""
        count = len(self.sp_g4.interactions)
        self.assertGreaterEqual(count, 25, f"Too few interactions: {count}")
        self.assertLessEqual(count, 35, f"Too many interactions: {count}")

    def test_phase_coverage(self):
        """All 4 phases should be present."""
        phases = set(ix.phase for ix in self.sp_g4.interactions)
        for expected in ("Warmup", "Lesson", "EC", "Synthesis"):
            self.assertIn(expected, phases, f"Missing phase: {expected}")

    def test_phase_interaction_counts(self):
        """Phase breakdown should match M7's known structure."""
        phase_counts = {}
        for ix in self.sp_g4.interactions:
            phase_counts[ix.phase] = phase_counts.get(ix.phase, 0) + 1

        self.assertEqual(phase_counts.get("Warmup"), 3, "Warmup should have 3 interactions")
        self.assertGreaterEqual(phase_counts.get("Lesson", 0), 15, "Lesson should have 15+ interactions")
        self.assertEqual(phase_counts.get("EC"), 3, "EC should have 3 interactions")
        self.assertGreaterEqual(phase_counts.get("Synthesis", 0), 4, "Synthesis should have 4+ interactions")

    def test_pattern_detection(self):
        """Parser should correctly classify interaction patterns."""
        patterns = {}
        for ix in self.sp_g4.interactions:
            patterns[ix.pattern] = patterns.get(ix.pattern, 0) + 1

        # M7 should have a mix of student_action and teaching_only
        self.assertGreater(patterns.get("student_action", 0), 10,
                           "Should have >10 student_action interactions")
        self.assertGreater(patterns.get("teaching_only", 0), 2,
                           "Should have >2 teaching_only interactions")
        # No interactions should be 'unknown' after parser fix
        self.assertEqual(patterns.get("unknown", 0), 0,
                         f"Found {patterns.get('unknown', 0)} 'unknown' pattern interactions — parser regression")

    def test_dash_bullet_normalization(self):
        """Parser should handle both - ** and * ** bullet formats."""
        # M7 Notion-pulled uses dash bullets. All interactions should be detected.
        for ix in self.sp_g4.interactions:
            if ix.pattern == "student_action":
                self.assertTrue(ix.has_guide,
                    f"{ix.id} ({ix.phase}): student_action missing Guide")

    def test_dialogue_extraction(self):
        """Parser should extract dialogue lines from interactions."""
        total_dialogue = sum(len(ix.dialogue_lines) for ix in self.sp_g4.interactions)
        self.assertGreater(total_dialogue, 20,
                           f"Only {total_dialogue} dialogue lines extracted — expected 20+")

    def test_interaction_ids(self):
        """Interaction IDs should follow expected patterns."""
        ids = [ix.id for ix in self.sp_g4.interactions]
        # Warmup IDs
        self.assertIn("W.1", ids)
        self.assertIn("W.2", ids)
        self.assertIn("W.3", ids)
        # Lesson IDs (at least some)
        self.assertIn("1.1", ids)
        self.assertIn("2.0", ids)
        self.assertIn("3.0", ids)
        # EC IDs
        self.assertIn("EC.1", ids)
        # Synthesis IDs
        self.assertIn("S.1", ids)

    def test_gate_filtering(self):
        """Gate filtering should progressively include more phases."""
        from sp_parse_interactions import filter_by_gate

        g1 = filter_by_gate(self.sp, 1)
        g2 = filter_by_gate(self.sp, 2)
        g3 = filter_by_gate(self.sp, 3)
        g4 = filter_by_gate(self.sp, 4)

        self.assertEqual(len(g1.interactions), 0, "Gate 1 should have 0 interactions")
        self.assertGreater(len(g2.interactions), 0, "Gate 2 should have interactions")
        self.assertGreater(len(g3.interactions), len(g2.interactions),
                           "Gate 3 should have more interactions than Gate 2")
        self.assertGreaterEqual(len(g4.interactions), len(g3.interactions),
                                "Gate 4 should have >= Gate 3 interactions")


# ---------------------------------------------------------------------------
# Test: All Checkers Run Without Error
# ---------------------------------------------------------------------------

class TestCheckersRunClean(unittest.TestCase):
    """Verify every checker runs without crashing at all gate levels."""

    CHECKERS = [
        ("sp_structure_check", "run_structure_check"),
        ("sp_vocab_scan", "run_vocab_scan"),
        ("sp_voice_scan", "run_voice_scan"),
        ("sp_interaction_check", "run_interaction_check"),
        ("sp_timing_estimate", "run_timing_estimate"),
        ("sp_toy_consistency", "run_toy_check"),
        ("sp_dimension_track", "run_dimension_track"),
        ("sp_module_map_check", "run_module_map_check"),
    ]

    @classmethod
    def setUpClass(cls):
        if not os.path.exists(M7_FILE):
            raise unittest.SkipTest("Golden file not found")

    def _run_checker(self, module_name, func_name, gate):
        """Import and run a checker, returning the result dict."""
        mod = __import__(module_name)
        func = getattr(mod, func_name)
        result = func(M7_FILE, gate)
        return result

    def _assert_valid_result(self, result, checker_name, gate):
        """Verify the result dict has the expected structure."""
        self.assertIsInstance(result, dict, f"{checker_name} gate {gate} didn't return dict")
        for key in ("checker", "file", "gate", "findings", "total_findings"):
            self.assertIn(key, result, f"{checker_name} gate {gate} missing '{key}'")
        self.assertEqual(result["gate"], gate)
        self.assertIsInstance(result["findings"], list)
        self.assertEqual(result["total_findings"], len(result["findings"]))

    def test_all_checkers_gate1(self):
        for mod_name, func_name in self.CHECKERS:
            with self.subTest(checker=mod_name):
                result = self._run_checker(mod_name, func_name, 1)
                self._assert_valid_result(result, mod_name, 1)

    def test_all_checkers_gate2(self):
        for mod_name, func_name in self.CHECKERS:
            with self.subTest(checker=mod_name):
                result = self._run_checker(mod_name, func_name, 2)
                self._assert_valid_result(result, mod_name, 2)

    def test_all_checkers_gate3(self):
        for mod_name, func_name in self.CHECKERS:
            with self.subTest(checker=mod_name):
                result = self._run_checker(mod_name, func_name, 3)
                self._assert_valid_result(result, mod_name, 3)

    def test_all_checkers_gate4(self):
        for mod_name, func_name in self.CHECKERS:
            with self.subTest(checker=mod_name):
                result = self._run_checker(mod_name, func_name, 4)
                self._assert_valid_result(result, mod_name, 4)


# ---------------------------------------------------------------------------
# Test: Interaction Checker Specific Findings
# ---------------------------------------------------------------------------

class TestInteractionChecker(unittest.TestCase):
    """Verify interaction checker produces expected findings on M7."""

    @classmethod
    def setUpClass(cls):
        if not os.path.exists(M7_FILE):
            raise unittest.SkipTest("Golden file not found")
        from sp_interaction_check import run_interaction_check
        cls.result = run_interaction_check(M7_FILE, 4)

    def test_no_critical_findings(self):
        """M7 (Gate 4 PASS) should have no CRITICAL interaction findings."""
        crits = [f for f in self.result["findings"] if f["severity"] == "CRITICAL"]
        self.assertEqual(len(crits), 0,
                         f"Unexpected CRITICAL findings: {[f['detail'] for f in crits]}")

    def test_no_unknown_pattern_findings(self):
        """No I0 (unknown pattern) findings after parser fix."""
        i0s = [f for f in self.result["findings"] if f["check"] == "I0"]
        self.assertEqual(len(i0s), 0,
                         f"Found {len(i0s)} I0 findings — parser regression")

    def test_on_correct_length_findings(self):
        """I20 should fire on M7's known verbose On Correct lines."""
        i20s = [f for f in self.result["findings"] if f["check"] == "I20"]
        self.assertGreater(len(i20s), 0, "Expected some I20 (On Correct length) findings")
        # M7 has several verbose On Correct lines (W.2, 1.3, 1.5, 2.1, etc.)
        self.assertGreaterEqual(len(i20s), 3,
                                f"Expected 3+ I20 findings, got {len(i20s)}")

    def test_phase_breakdown_in_meta(self):
        """Meta should contain phase breakdown."""
        breakdown = self.result["meta"].get("phase_breakdown", {})
        self.assertIn("Warmup", breakdown)
        self.assertIn("Lesson", breakdown)
        self.assertIn("EC", breakdown)
        self.assertIn("Synthesis", breakdown)


# ---------------------------------------------------------------------------
# Test: Voice Scanner Specific Findings
# ---------------------------------------------------------------------------

class TestVoiceScanner(unittest.TestCase):
    """Verify voice scanner produces expected findings on M7."""

    @classmethod
    def setUpClass(cls):
        if not os.path.exists(M7_FILE):
            raise unittest.SkipTest("Golden file not found")
        from sp_voice_scan import run_voice_scan
        cls.result = run_voice_scan(M7_FILE, 4)

    def test_no_critical_findings(self):
        """M7 should have no CRITICAL voice findings."""
        crits = [f for f in self.result["findings"] if f["severity"] == "CRITICAL"]
        self.assertEqual(len(crits), 0,
                         f"Unexpected CRITICAL findings: {[f['detail'] for f in crits]}")

    def test_verbose_guide_findings(self):
        """VO4 (verbose Guide) should fire — M7 has long Guide lines in S1/S2/S3."""
        vo4s = [f for f in self.result["findings"] if f["check"] == "VO4"]
        self.assertGreater(len(vo4s), 0, "Expected some VO4 findings for verbose Guide lines")

    def test_dialogue_lines_scanned(self):
        """Should scan a meaningful number of dialogue lines."""
        scanned = self.result["meta"].get("dialogue_lines_scanned", 0)
        self.assertGreater(scanned, 20,
                           f"Only {scanned} dialogue lines scanned — parser may not be extracting")


# ---------------------------------------------------------------------------
# Test: Dimension Tracker
# ---------------------------------------------------------------------------

class TestDimensionTracker(unittest.TestCase):
    """Verify dimension tracker extracts values and finds cross-phase reuse."""

    @classmethod
    def setUpClass(cls):
        if not os.path.exists(M7_FILE):
            raise unittest.SkipTest("Golden file not found")
        from sp_dimension_track import run_dimension_track
        cls.result = run_dimension_track(M7_FILE, 4)

    def test_usage_table_populated(self):
        """Should find dimensions in multiple interactions."""
        usage = self.result["meta"].get("usage_table", [])
        self.assertGreater(len(usage), 20,
                           f"Only {len(usage)} interactions with values — expected 20+")

    def test_cross_phase_findings(self):
        """DT4/DT5 findings should exist — M7 has known dimension reuse."""
        dt_findings = [f for f in self.result["findings"]
                       if f["check"] in ("DT4", "DT5")]
        self.assertGreater(len(dt_findings), 0,
                           "Expected cross-phase dimension reuse findings")

    def test_working_notes_integration(self):
        """The --working-notes format_dimension_section should produce valid markdown."""
        from sp_dimension_track import format_dimension_section
        md = format_dimension_section(self.result)
        self.assertTrue(md.startswith("## DIMENSION TRACKING"))
        self.assertIn("Usage Table", md)


# ---------------------------------------------------------------------------
# Test: Structure Checker
# ---------------------------------------------------------------------------

class TestStructureChecker(unittest.TestCase):
    """Verify structure checker on M7 (known clean structure)."""

    @classmethod
    def setUpClass(cls):
        if not os.path.exists(M7_FILE):
            raise unittest.SkipTest("Golden file not found")
        from sp_structure_check import run_structure_check
        cls.result = run_structure_check(M7_FILE, 4)

    def test_no_critical_findings(self):
        """M7 should have no CRITICAL structural findings."""
        crits = [f for f in self.result["findings"] if f["severity"] == "CRITICAL"]
        self.assertEqual(len(crits), 0,
                         f"Unexpected CRITICAL: {[f['detail'] for f in crits]}")

    def test_clean_structure(self):
        """M7 passed Gate 4 — should have minimal structural issues."""
        # Allow some minor findings but no majors
        majors = [f for f in self.result["findings"] if f["severity"] == "MAJOR"]
        self.assertLessEqual(len(majors), 2,
                             f"Too many MAJOR structural findings for a Gate 4 PASS file: {len(majors)}")


# ---------------------------------------------------------------------------
# Test: Timing Estimator
# ---------------------------------------------------------------------------

class TestTimingEstimator(unittest.TestCase):
    """Verify timing estimates are reasonable."""

    @classmethod
    def setUpClass(cls):
        if not os.path.exists(M7_FILE):
            raise unittest.SkipTest("Golden file not found")
        from sp_timing_estimate import run_timing_estimate
        cls.result = run_timing_estimate(M7_FILE, 4)

    def test_session_total_reasonable(self):
        """Total session time should be in a reasonable range."""
        meta = self.result.get("meta", {})
        total_min = meta.get("session_total_min", 0)
        total_max = meta.get("session_total_max", 0)
        # A module should be roughly 10-30 minutes
        self.assertGreater(total_min, 5, f"Session min too low: {total_min}")
        self.assertLess(total_max, 45, f"Session max too high: {total_max}")


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main()
