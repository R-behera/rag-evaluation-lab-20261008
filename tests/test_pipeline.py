import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from rag_evaluation.pipeline import Pipeline


class PipelineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pipeline = Pipeline.from_file(ROOT / "artifacts" / "model.json")

    def test_model_metadata(self):
        self.assertEqual(self.pipeline.model["project"], "rag-evaluation")
        self.assertTrue(self.pipeline.model["trained_on_synthetic_data"])

    def test_prediction_and_evidence(self):
        result = self.pipeline.run("The expected document never appeared in the top results")
        self.assertIn(result["prediction"], ["retrieval-miss","unsupported-answer","citation-gap","abstention-error"])
        self.assertGreaterEqual(len(result["evidence"]), 1)
        evidence_ids = [item["id"] for item in result["evidence"]]
        self.assertEqual(len(evidence_ids), len(set(evidence_ids)))
        self.assertIn("requires_review", result)


if __name__ == "__main__":
    unittest.main()
