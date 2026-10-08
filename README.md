# RAG Evaluation Lab

A reproducible RAG evaluation harness for retrieval misses, unsupported answers, citation gaps, and abstention errors.

Generated on 2026-10-08 as an independent production-AI architecture project.

## Real-World Problem

RAG systems often ship without a stable regression set or failure taxonomy.

## Hugging Face Tasks

- `text-classification`
- `question-answering`
- `text-ranking`
- `summarization`

## Recommended Production Stack

- FastAPI for evaluation jobs and reports
- Ragas-style retrieval and faithfulness metrics
- MLflow for experiment and artifact tracking
- PostgreSQL for versioned evaluation cases
- OpenTelemetry plus Phoenix for trace inspection
- GitHub Actions for threshold-based release gates

## Included

- Runnable Python pipeline with no runtime dependencies
- Local JSON HTTP inference service
- Public-data API connector with explicit provenance
- Reproducible training script
- Held-out evaluation command
- Synthetic dataset with explicit provenance
- Trained transparent baseline model
- Architecture and production-boundary documentation
- Unit tests, CI workflow, and Dockerfile
- Hugging Face-ready model and dataset cards

## Architecture

1. Versioned evaluation cases
1. Failure-mode classifier
1. Retrieval and answer metrics
1. Threshold-based release gate
1. Markdown evaluation report

See [ARCHITECTURE.md](ARCHITECTURE.md) for the full flow and production
boundaries.

## Quick Start

```bash
python3 -m unittest discover -s tests
PYTHONPATH=src python3 -m rag_evaluation.cli "The expected document never appeared in the top results"
PYTHONPATH=src python3 evaluate.py
PYTHONPATH=src python3 -m rag_evaluation.service
```

The service exposes `GET /health` and `POST /predict`.

Rebuild the model:

```bash
python3 train.py
```

## Baseline Evaluation

- Held-out synthetic examples: 4
- Accuracy: 0.75
- Target metrics: failure_class_accuracy, citation_coverage, release_gate_pass_rate

This score verifies that the code and evaluation contract work. It does not
claim production performance.

## Hugging Face Artifacts

When the controller has a Hugging Face token and namespace configured, it
publishes:

- Dataset: `rag-evaluation-lab-20261008-dataset`
- Model: `rag-evaluation-lab-20261008-model`

## Portfolio Value

This repository maps to production AI engineering work in:

- LLM and RAG evaluation design
- Golden datasets and failure taxonomies
- Experiment tracking and model release gates
- Trace-level diagnosis and prompt regression testing
- Statistical comparison of AI system versions

See [PORTFOLIO.md](PORTFOLIO.md) for resume-ready impact targets and interview
discussion areas.

## 1-3 Month Expansion

Follow [ROADMAP.md](ROADMAP.md) to add real-world APIs, a stronger open model,
durable orchestration, evaluation, observability, scalability testing, and a
public deployment.

## Safety

Synthetic cases validate the harness, not a production RAG system. Teams must add representative domain examples.

Review [ARCHITECTURE.md](ARCHITECTURE.md),
[PRODUCTION.md](PRODUCTION.md), [SECURITY.md](SECURITY.md),
[MODEL_CARD.md](MODEL_CARD.md), and [DATASET_CARD.md](DATASET_CARD.md) before
adapting this project.
