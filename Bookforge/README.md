# Bookforge

Bookforge is a staged literary generation engine designed to produce fiction through controlled planning, drafting, and validation pipelines.

The system is designed to operate locally using Ollama-hosted models, beginning with smaller models (such as qwen3:8b) and optionally scaling to larger models for validation tasks.

Bookforge prioritizes:

- structured planning before drafting
- canon adherence
- deterministic artifact pipelines
- gated validation at every stage
- bounded automated repair
- human intervention capability
- reproducible outputs

Bookforge supports fiction formats including:

- short stories
- novellas
- novels
- serialized fiction
- multi-book series

The system operates in phases:

1. Foundation
2. Story planning
3. Scene packet generation
4. Drafting + validation
5. Project orchestration
6. Graphical interface
7. Parallel execution
8. Series support

All writable operations must occur within `Bookforge/`.