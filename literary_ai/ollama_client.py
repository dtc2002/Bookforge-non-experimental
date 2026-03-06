import requests
from datetime import datetime
from typing import Dict, Any

class OllamaClient:
    def __init__(self, base_url: str = "http://localhost:11434", timeout: float = 30.0):
        self.base_url = base_url
        self.timeout = timeout

    def _request(self, method: str, endpoint: str, data: Dict = None) -> Dict:
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.request(
                method=method,
                url=url,
                json=data,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            error_msg = f"Request failed: {str(e)}"
            print(f"[ERROR] {error_msg}")
            raise RuntimeError(error_msg)

    def generate(self, model: str, prompt: str) -> Dict:
        return self._request("POST", "/api/generate", {
            "model": model,
            "prompt": prompt,
            "stream": False
        })