# Bookforge Architecture

Layers:

Engine Layer
Core generation logic

Service Layer
Callable operations for pipeline stages

Interface Layer
CLI initially
GUI later

Artifacts drive all operations.
Models never rely on conversation memory.

## Future Execution Model

Bookforge is initially single-runner and local-first.

Pipeline stages must be implemented as modular, artifact-driven jobs so they can later be dispatched across multiple runners without redesigning the core engine.

Model access must remain behind a client abstraction.