from passes import generate_scene_drafts
from drafts import save_drafts
import typer
from typing import List, Dict, Any

app = typer.Typer()

@app.command()
def draft_scenes(
    story_context: str = typer.Argument(..., help="Story context for scene drafting")
):
    """
    Generate literary scenes using the AI orchestrator
    """
    # Implement CLI integration with the orchestrator workflow
    drafts = generate_scene_drafts(story_context, ["Protagonist", "Antagonist"])
    save_drafts(drafts)
    print("Scene drafts generated and saved to database")

if __name__ == "__main__":
    app()