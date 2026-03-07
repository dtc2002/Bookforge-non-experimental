# Service Contracts

Bookforge should expose reusable service functions that can be called by the CLI now and GUI later.

Early target operations:

- create_project
- load_project
- run_brief_to_skeleton
- run_skeleton_to_beats
- run_beats_to_chapters
- run_planning_review
- run_smoke_test

## Rules

- CLI should call services, not contain core business logic.
- GUI should later call the same services.
- Services should operate on artifacts and manifests, not hidden in-memory state.