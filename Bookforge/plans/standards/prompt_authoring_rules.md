# Prompt Authoring Rules

Runtime prompts must remain short, specific, and schema-bound.

## Rules

- One job per prompt
- Explicit input artifact types
- Explicit output schema target
- No motivational or decorative language
- No builder-agent instructions in runtime prompts
- No markdown in JSON-returning prompts
- End JSON prompts with strict output requirements

## Small-model guidance

For smaller models such as qwen3:8b:

- keep instructions compact
- prefer direct field generation over long reasoning
- avoid asking for prose plus structure in the same prompt
- prefer multiple narrow passes over one overloaded pass