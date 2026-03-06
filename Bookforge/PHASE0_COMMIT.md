# Bookforge Phase 0 Commit

## Directory Structure
```
Bookforge/
├── pyproject.toml
├── literary_ai/
│   ├── __init__.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── artifact.py
│   │   ├── chapter.py
│   │   └── book.py
│   ├── ollama_client.py
│   └── sqlite_store.py
│   └── cli.py
├── tests/
└── README.md
```

## Implementation Details
- Ollama HTTP integration via `ollama_client.py`
- SQLite storage stub in `sqlite_store.py`
- Typer CLI with init/status commands in `cli.py`
- Artifact schemas in `schemas/`

## Verification
```
pip install -e .
pytest
bookforge --help
bookforge init
bookforge status
```
