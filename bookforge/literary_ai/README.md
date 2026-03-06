# literary_ai

## Overview

This is a Python package for working with literary AI, including Ollama integration, artifact management, and a CLI interface.

## Structure

```
/bookforge/
  /literary_ai/
    /schemas/
    /store/
    /cli/
    ollama_client.py
    pyproject.toml
    README.md
```

## Installation

```bash
pip install -e .
```

## Usage

### CLI Commands

- `literary_ai init` - Initialize the SQLite database
- `literary_ai status` - Check the database status

### API

Use the OllamaClient to interact with Ollama models:

```python
from literary_ai.ollama_client import OllamaClient

async def main():
    async with OllamaClient() as client:
        response = await client.generate("llama3", "Hello, world!")
        print(response)

if __name__ == "__main__":
    asyncio.run(main())
```

## Testing

Run tests with:

```bash
pytest
```

## Development

Make sure to run:

```bash
typer --install
typer --check
```

This will install and check the CLI commands.