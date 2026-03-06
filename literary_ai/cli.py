from typer import Typer, Option
from rich import print
from pathlib import Path

typer_app = Typer()

@typer_app.command()
def init(
    name: str = Option(..., prompt="Project name:")
):
    """Initialize a new literary AI project."""
    project_dir = Path(name)
    project_dir.mkdir(exist_ok=True)
    
    # Create necessary directories
    (project_dir / "stories").mkdir(exist_ok=True)
    (project_dir / "characters").mkdir(exist_ok=True)
    (project_dir / "canon").mkdir(exist_ok=True)
    
    # Create config files
    config = {
        "name": name,
        "author": "Your Name",
        "settings": {}
    }
    
    # Write config file
    with (project_dir / "config.json").open('w') as f:
        json.dump(config, f, indent=2)
    
    print(f"[bold green]Initialized project {name}[/bold green]"
          f"\nCreated directories: {', '.join(project_dir.iterdir())}")

@typer_app.command()
def status():
    """Show project status."""
    print("[bold blue]Project Status[/bold blue]")
    print("- Check database connections")
    print("- Verify file structures")
    print("- Review configuration files")

@typer_app.command()
def pipeline():
    """Run the literary AI pipeline."""
    print("[bold magenta]Running literary AI pipeline[/bold magenta]")
    print("1. Analyzing story structure")
    print("2. Generating character profiles")
    print("3. Validating canon facts")
    print("4. Checking for inconsistencies")

if __name__ == "__main__":
    typer_app()

# Add more pipeline commands as needed