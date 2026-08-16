from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MOCKS = ROOT / "mocks"


class PublicFixtureTests(unittest.TestCase):
    def load_fixture(self, name: str) -> dict[str, object]:
        return json.loads((MOCKS / name).read_text(encoding="utf-8"))

    def test_available_fixture_is_synthetic_and_actionable(self) -> None:
        fixture = self.load_fixture("installment_limit_available.json")

        self.assertEqual(fixture["fixtureScope"], "synthetic-portfolio-example")
        self.assertEqual(fixture["status"], "AVAILABLE")
        self.assertGreater(fixture["availableAmount"], 0)
        self.assertTrue(fixture["primaryActionEnabled"])

    def test_overdue_fixture_blocks_primary_action(self) -> None:
        fixture = self.load_fixture("installment_limit_overdue.json")

        self.assertEqual(fixture["fixtureScope"], "synthetic-portfolio-example")
        self.assertEqual(fixture["status"], "OVERDUE")
        self.assertGreater(fixture["overdueAmount"], 0)
        self.assertFalse(fixture["primaryActionEnabled"])


if __name__ == "__main__":
    unittest.main()

