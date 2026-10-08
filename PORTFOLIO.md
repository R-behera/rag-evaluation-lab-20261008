# Portfolio and Career Mapping

## Project Pitch

**RAG Evaluation Lab** solves this real-world problem:

RAG systems often ship without a stable regression set or failure taxonomy.

It combines `text-classification`, `question-answering`, `text-ranking`, `summarization` with data ingestion, evaluation, observability, and scalable
service design.

## Why This Is More Than an API Wrapper

- Owns ingestion, validation, model artifacts, and evaluation datasets.
- Exposes evidence and confidence instead of returning opaque text.
- Includes offline evaluation and a CI release gate.
- Defines tracing, rollback, human review, and failure recovery.
- Provides a realistic path from free local baseline to production stack.

## AI Engineering Job Description Mapping

- LLM and RAG evaluation design
- Golden datasets and failure taxonomies
- Experiment tracking and model release gates
- Trace-level diagnosis and prompt regression testing
- Statistical comparison of AI system versions

## Resume-Ready Impact Targets

Replace targets with measured results after completing the roadmap:

- Detect 100% of seeded unsupported-answer regressions
- Track retrieval, faithfulness, citation, latency, and cost metrics
- Fail CI when any critical metric drops beyond tolerance
- Produce comparable evaluation reports for every model version

Example resume format:

> Built RAG Evaluation Lab, a production-oriented ai-evaluation system
> using FastAPI for evaluation jobs and reports, Ragas-style retrieval and faithfulness metrics, MLflow for experiment and artifact tracking; measured
> failure_class_accuracy, citation_coverage, release_gate_pass_rate and
> enforced regression thresholds in CI.

## Interview Discussion Areas

- Why this architecture fits the problem and where it fails
- Retrieval/model choice and baseline comparisons
- Evaluation-set construction and metric trade-offs
- Data privacy, authorization, and human escalation
- Scaling, caching, index tuning, and failure recovery
- Model, prompt, dataset, and deployment lineage
