import typer
from .schemas.book import Book
from .store.sqlite_store import SQLiteStore
from .ollama_client import OllamaClient
import asyncio

app = typer.Typer()

@app.command()
def init():
    """Initialize the SQLite database."""
    store = SQLiteStore()
    try:
        # Create tables
        store.get_db().commit()
        typer.echo("Database initialized successfully.")
    except Exception as e:
        typer.echo(f"Failed to initialize database: {str(e)}")

@app.command()
def status():
    """Check the status of the SQLite database."""
    store = SQLiteStore()
    try:
        # Check if database exists
        with sqlite3.connect('literary_ai.db') as conn:
            conn.execute('SELECT 1')
        typer.echo("Database is running and accessible.")
    except Exception as e:
        typer.echo(f"Database connection failed: {str(e)}")

if __name__ == "__main__":
    app()