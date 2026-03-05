import httpx
from typing import Optional, Dict, List

class OllamaClient:
    def __init__(self, base_url: str = "http://localhost:11434"):
        self.base_url = base_url
        self.client = httpx.Client(base_url=self.base_url)

    async def list_models(self) -> List[str]:
        response = await self.client.get("/api/tags")
        return [model['name'] for model in response.json()['models']]

    async def generate(self, model: str, prompt: str) -> Dict:
        response = await self.client.post("/api/generate", json={"model": model, "prompt": prompt})
        return response.json()