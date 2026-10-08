---
license: cc-by-4.0
language:
- en
pretty_name: RAG Evaluation Lab Synthetic Evaluation Set
size_categories:
- n<1K
task_categories:
- text-classification
tags:
- synthetic
- ai-evaluation
- evaluation
- text-classification
- question-answering
- text-ranking
- summarization
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train.jsonl
  - split: test
    path: data/test.jsonl
---

# RAG Evaluation Lab Synthetic Dataset

## Summary

This dataset contains 14 training examples and 4
held-out examples for **RAG systems often ship without a stable regression set or failure taxonomy.**

Every record is synthetic and includes:

- `input`: query, event, or feature description
- `label`: expected class, route, relation, or evidence category
- `context`: synthetic supporting context
- `source`: fictional source identifier
- `variant`: generation pattern
- `synthetic`: always `true`

## Uses

- Reproducible unit and integration tests
- Baseline model training
- Evaluation harness development
- Schema and architecture demonstrations

## Limitations

Synthetic cases validate the harness, not a production RAG system. Teams must add representative domain examples.

This dataset does not represent real users, patients, customers, production
traffic, or licensed media. It must not be presented as real-world evidence.

## Related Model

[{{HF_NAMESPACE}}/rag-evaluation-lab-20261008-model](https://huggingface.co/{{HF_NAMESPACE}}/rag-evaluation-lab-20261008-model)
