import httpx
import asyncio
from typing import Optional, Dict, Any

class OllamaClient:
    def __init__(self, base_url: str = "http://localhost:11434", timeout: float = 30.0):
        self.base_url = base_url
        self.timeout = timeout
        self.client = httpx.AsyncClient(timeout=self.timeout)

    async def generate(self, model: str, prompt: str) -> Dict[str, Any]:
        try:
            response = await self.client.post(
                f"{self.base_url}/api/generate",
                json={"model": model, "prompt": prompt, "stream": False},
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except httpx.RequestError as e:
            print(f"HTTP error occurred: {e}")
            return {"error": str(e)}
        except Exception as e:
            print(f"An error occurred: {e}")
            return {"error": str(e)}

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.client.aclose()

    def close(self):
        self.client.close()

    def __del__(self):
        self.close()