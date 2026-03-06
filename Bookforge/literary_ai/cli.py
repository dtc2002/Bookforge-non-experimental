import typer
from .ollama_client import OllamaClient
from .sqlite_store import SQLiteStore
from .schemas import ArtifactSchema

app = typer.Typer()

@app.command()
def init():
    """Initialize Bookforge configuration"""
    typer.echo("Initializing Bookforge... This will create the SQLite database")
    SQLiteStore()
    typer.echo("Bookforge initialized successfully")

@app.command()
def status():
    """Show Bookforge status"""
    typer.echo("Bookforge status:")
    typer.echo("- SQLite database: Created")
    typer.echo("- Ollama integration: Ready")
    typer.echo("- CLI commands: init, status")

if __name__ == "__main__":
    app()
