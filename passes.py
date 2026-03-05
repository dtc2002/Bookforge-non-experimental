import httpx
from typing import List, Dict, Any
from datetime import datetime

async def generate_scene_drafts(story_context: str, characters: List[str], model: str = "llama3") -> List[Dict[str, Any]]:
    """
    Generate scene drafts using Ollama
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://ollama:11434/api/generate",
            json={
                "model": model,
                "prompt": f"Write scene drafts for a story about {story_context} with characters {', '.join(characters)}. Include beat-by-beat dialogue and action.",
                "stream": False
            }
        )
        response.raise_for_status()
        
        drafts = []
        for line in response.json()["response"].split("\n\n"):
            if line.strip():
                scene = {
                    "scene_number": len(drafts) + 1,
                    "timestamp": datetime.now().isoformat(),
                    "content": line.strip(),
                    "characters": characters
                }
                drafts.append(scene)
        return drafts

# Add to orchestrator workflow
# Orchestrator will handle repair loops and integration with checker systems