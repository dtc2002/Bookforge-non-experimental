import requests
import json
from typing import List, Dict, Any

class OllamaClient:
    def __init__(self, base_url: str = "http://localhost:11434"):
        self.base_url = base_url

    def list_models(self) -> Dict[str, Any]:
        """List available models"""
        response = requests.get(f"{self.base_url}/api/v1/models")
        return response.json()

    def generate(self, model: str, prompt: str, options: Dict[str, Any] = {}) -> Dict[str, Any]:
        """Generate text using a model"""
        response = requests.post(
            f"{self.base_url}/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "options": options
            }
        )
        return response.json()

    def chat(self, model: str, messages: List[Dict[str, str]], options: Dict[str, Any] = {}) -> Dict[str, Any]:
        """Maintain a chat conversation"""
        response = requests.post(
            f"{self.base_url}/api/chat",
            json={
                "model": model,
                "messages": messages,
                "options": options
            }
        )
        return response.json()
