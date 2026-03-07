# Architecture Boundaries

Bookforge must maintain clear boundaries between system layers.

## Builder layer
Used only by PopeBot to implement the repository.

Includes:
- plans
- task files
- standards for implementation
- PR rules

## Runtime engine layer
Used by Bookforge during operation.

Includes:
- planning modules
- drafting modules
- validation modules
- artifact management
- project manifest management
- model client access

## Interface layer
Used by the operator.

Includes:
- CLI during early development
- GUI in later phases

## Rules

- Builder instructions must not leak into runtime prompts.
- Runtime prompts must not assume PopeBot behavior.
- GUI logic must not contain core planning logic.
- Model access must remain behind a reusable client abstraction.
- Pipeline state must be artifact-driven, not memory-driven.