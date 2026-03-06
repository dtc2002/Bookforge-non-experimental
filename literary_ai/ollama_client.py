import httpx
from pydantic import BaseModel
from typing import Optional
import asyncio
import os
from rich.progress import Progress,TaskDescription
from datetime import datetime
from contextlib import asynccontextmanager
from contextvars import ContextVar
from urllib.parse import urlparse

# Context for tracking request context
request_context = ContextVar("request_context", default={})

class OllamaClient:
    def __init__(self, base_url: str = "http://localhost:11434", timeout: float = 30.0):
        self.base_url = base_url
        self.timeout = timeout
        self.client = httpx.AsyncClient(timeout=timeout)
        self._auth_token = os.environ.get("OLLAMA_AUTH_TOKEN")
        self._model_cache = {}  # Cache model info

    async def _get_model_info(self, model_name: str) -> dict:
        if model_name in self._model_cache:
            return self._model_cache[model_name]

        url = f"{self.base_url}/api/v1/models/{model_name}"
        headers = {} if not self._auth_token else {"Authorization": f"Bearer {self._auth_token}"}
        try:
            async with self.client.stream("GET", url, headers=headers) as response:
                if response.status_code != 200:
                    raise Exception(f"Model {model_name} not found: {await response.text()}")
                
                model_info = await response.json()
                self._model_cache[model_name] = model_info
                return model_info
        except Exception as e:
            raise RuntimeError(f"Failed to get model info for {model_name}: {str(e)}") from e

    async def list_models(self) -> list:
        url = f"{self.base_url}/api/v1/models"
        headers = {} if not self._auth_token else {"Authorization": f"Bearer {self._auth_token}"}
        try:
            async with self.client.stream("GET", url, headers=headers) as response:
                if response.status_code != 200:
                    raise Exception(f"Failed to list models: {await response.text()}")
                return [model['name'] for model in await response.json()]
        except Exception as e:
            raise RuntimeError(f"Failed to list models: {str(e)}") from e

    async def create_model(self, model_name: str, from_model: str) -> dict:
        url = f"{self.base_url}/api/v1/models"
        headers = {} if not self._auth_token else {"Authorization": f"Bearer {self._auth_token}"}
        payload = {
            "name": model_name,
            "from": from_model
        }
        try:
            async with self.client.stream("POST", url, headers=headers, json=payload) as response:
                if response.status_code != 200:
                    raise Exception(f"Failed to create model {model_name}: {await response.text()}")
                return await response.json()
        except Exception as e:
            raise RuntimeError(f"Failed to create model {model_name}: {str(e)}") from e

    async def pull_model(self, model_name: str, stream: bool = False) -> dict:
        url = f"{self.base_url}/api/v1/models/{model_name}/pull"
        headers = {} if not self._auth_token else {"Authorization": f"Bearer {self._auth_token}"}
        params = {"stream": stream}
        try:
            async with self.client.stream("POST", url, headers=headers, params=params) as response:
                if response.status_code != 200:
                    raise Exception(f"Failed to pull model {model_name}: {await response.text()}")
                return await response.json()
        except Exception as e:
            raise RuntimeError(f"Failed to pull model {model_name}: {str(e)}") from e

    async def generate(self, model_name: str, prompt: str, options: dict = None, stream: bool = False) -> dict:
        url = f"{self.base_url}/api/v1/generate"
        headers = {} if not self._auth_token else {"Authorization": f"Bearer {self._auth_token}"}
        payload = {
            "model": model_name,
            "prompt": prompt,
            "options": options or {},
            "stream": stream
        }
        try:
            async with self.client.stream("POST", url, headers=headers, json=payload) as response:
                if response.status_code != 200:
                    raise Exception(f"Generation failed: {await response.text()}")
                
                if stream:
                    async def stream_generator():
                        async for chunk in response.aiter_bytes():
                            yield chunk
                    return stream_generator()
                
                return await response.json()
        except Exception as e:
            raise RuntimeError(f"Generation failed: {str(e)}") from e

    async def chat(self, model_name: str, messages: list, options: dict = None) -> dict:
        url = f"{self.base_url}/api/v1/chat"
        headers = {} if not self._auth_token else {"Authorization": f"Bearer {self._auth_token}"}
        payload = {
            "model": model_name,
            "messages": messages,
            "options": options or {}
        }
        try:
            async with self.client.stream("POST", url, headers=headers, json=payload) as response:
                if response.status_code != 200:
                    raise Exception(f"Chat failed: {await response.text()}")
                return await response.json()
        except Exception as e:
            raise RuntimeError(f"Chat failed: {str(e)}") from e

    async def modelfile(self, model_name: str, content: str, stream: bool = False) -> dict:
        url = f"{self.base_url}/api/v1/models/{model_name}/modelfile"
        headers = {} if not self._auth_token else {"Authorization": f"Bearer {self._auth_token}"}
        params = {"stream": stream}
        try:
            async with self.client.stream("POST", url, headers=headers, params=params, data=content) as response:
                if response.status_code != 200:
                    raise Exception(f"Modelfile operation failed: {await response.text()}")
                return await response.json()
        except Exception as e:
            raise RuntimeError(f"Modelfile operation failed: {str(e)}") from e

    async def delete_model(self, model_name: str) -> bool:
        url = f"{self.base_url}/api/v1/models/{model_name}"
        headers = {} if not self._auth_token else {"Authorization": f"Bearer {self._auth_token}"}
        try:
            async with self.client.stream("DELETE", url, headers=headers) as response:
                if response.status_code != 200:
                    raise Exception(f"Failed to delete model {model_name}: {await response.text()}")
                return True
        except Exception as e:
            raise RuntimeError(f"Failed to delete model {model_name}: {str(e)}") from e

    async def get_model_info(self, model_name: str) -> dict:
        return await self._get_model_info(model_name)

    def __del__(self):
        if hasattr(self, "client"):
            self.client.aclose()

# Context manager for request tracking
@asynccontextmanager
async def request_context_manager(ctx: dict):
    token = request_context.set(ctx)
    try:
        yield
    finally:
        request_context.reset(token)

# Utility for parsing Ollama model info
def parse_model_info(model_info: dict) -> dict:
    return {
        "name": model_info.get("name"),
        "description": model_info.get("description"),
        "modified_at": model_info.get("modified_at"),
        "size": model_info.get("size"),
        "quantized": model_info.get("quantized"),
        "trained_at": model_info.get("trained_at"),
        "parent": model_info.get("parent"),
        "created_at": model_info.get("created_at"),
        "modified_by": model_info.get("modified_by"),
        "training": model_info.get("training"),
        "format": model_info.get("format"),
        "parameters": model_info.get("parameters"),
        "layers": model_info.get("layers"),
        "version": model_info.get("version"),
        "digest": model_info.get("digest")
    }

# Utility for parsing Ollama model list
def parse_model_list(model_list: list) -> list:
    return [{
        "name": model['name'],
        "description": model['description'],
        "modified_at": model['modified_at'],
        "size": model['size'],
        "quantized": model['quantized'],
        "trained_at": model['trained,trained_at'],
        "parent": model['parent'],
        "created_at": model['created_at'],
        "modified_by": model['modified_by'],
        "training": model['training'],
        "format": model['format'],
        "parameters": model['parameters'],
        "layers": model['layers'],
        "version": model['version'],
        "digest": model['digest']
    } for model in model_list]

# Utility for parsing Ollama generate response
def parse_generate_response(response: dict) -> dict:
    return {
        "response": response.get("response"),
        "candidate": response.get("candidate"),
        "context": response.get("context"),
        "total_duration": response.get("total_duration"),
        "prompt_duration": response.get("prompt_duration"),
        "generate_duration": response.get("generate_duration"),
        "eval_duration": response.get("eval_duration"),
        "model_name": response.get("model_name"),
        "created_at": response.get("created_at"),
        "modified_at": response.get("modified_at"),
        "model_version": response.get("model_version"),
        "model_size": response.get("model_size"),
        "model_format": response.get("model_format")
    }

# Utility for parsing Ollama chat response
def parse_chat_response(response: dict) -> dict:
    return {
        "response": response.get("response"),
        "candidate": response.get("candidate"),
        "context": response.get("context"),
        "total_duration": response.get("total_duration"),
        "prompt_duration": response.get("prompt_duration"),
        "generate_duration": response.get("generate_duration"),
        "eval_duration": response.get("eval_duration"),
        "model_name": response.get("model_name"),
        "created_at": response.get("created_at"),
        "modified_at": response.get("modified_at"),
        "model_version": response.get("model_version"),
        "model_size": response.get("model_size"),
        "model_format": response.get("model_format")
    }

# Utility for parsing Ollama pull model response
def parse_pull_model_response(response: dict) -> dict:
    return {
        "status": response.get("status"),
        "name": response.get("name"),
        "description": response.get("description"),
        "modified_at": response.get("modified_at"),
        "size": response.get("size"),
        "quantized": response.get("quantized"),
        "trained_at": response.get("trained_at"),
        "parent": response.get("parent"),
        "created_at": response.get("created_at"),
        "modified_by": response.get("modified_by"),
        "training": response.get("training"),
        "format": response.get("format"),
        "parameters": response.get("parameters"),
        "layers": response.get("layers"),
        "version": response.get("version"),
        "digest": response.get("digest")
    }

# Utility for parsing Ollama modelfile response
def parse_modelfile_response(response: dict) -> dict:
    return {
        "status": response.get("status"),
        "name": response.get("name"),
        "description": response.get("description"),
        "modified_at": response.get("modified_at"),
        "size": response.get("size"),
        "quantized": response.get("quantized"),
        "trained_at": response.get("trained_at"),
        "parent": response.get("parent"),
        "created_at": response.get("created_at"),
        "modified_by": response.get("modified_by"),
        "training": response.get("training"),
        "format": response.get("format"),
        "parameters": response.get("parameters"),
        "layers": response.get("layers"),
        "version": response.get("version"),
        "digest": response.get("digest")
    }

# Utility for parsing Ollama delete model response
def parse_delete_model_response(response: dict) -> bool:
    return response.get("deleted", False)

# Utility for parsing Ollama model info
def parse_model_info(model_info: dict) -> dict:
    return {
        "name": model_info.get("name"),
        "description": model_info.get("description"),
        "modified_at": model_info.get("modified_at"),
        "size": model_info.get("size"),
        "quantized": model_info.get("quantized"),
        "trained_at": model_info.get("trained_at"),
        "parent": model_info.get("parent"),
        "created_at": model_info.get("created_at"),
        "modified_by": model_info.get("modified_by"),
        "training": model_info.get("training"),
        "format": model_info.get("format"),
        "parameters": model_info.get("parameters"),
        "layers": model_info.get("layers"),
        "version": model_info.get("version"),
        "digest": model_info.get("digest")
    }

# Utility for parsing Ollama model list
def parse_model_list(model_list: list) -> list:
    return [{
        "name": model['name'],
        "description": model['description'],
        "modified_at": model['modified_at'],
        "size": model['size'],
        "quantized": model['quantized'],
        "trained_at": model['trained_at'],
        "parent": model['parent'],
        "created_at": model['created_at'],
        "modified_by": model['modified_by'],
        "training": model['training'],
        "format": model['format'],
        "parameters": model['parameters'],
        "layers": model['layers'],
        "version": model['version'],
        "digest": model['digest']
    } for model in model_list]

# Utility for parsing Ollama generate response
def parse_generate_response(response: dict) -> dict:
    return {
        "response": response.get("response"),
        "candidate": response.get("candidate"),
        "context": response.get("context"),
        "total_duration": response.get("total_duration"),
        "prompt_duration": response.get("prompt_duration"),
        "generate_duration": response.get("generate_duration"),
        "eval_duration": response.get("eval_duration"),
        "model_name": response.get("model_name"),
        "created_at": response.get("created_at"),
        "modified_at": response.get("modified_at"),
        "model_version": response.get("model_version"),
        "model_size": response.get("model_size"),
        "model_format": response.get("model_format")
    }

# Utility for parsing Ollama chat response
def parse_chat_response(response: dict) -> dict:
    return {
        "response": response.get("response"),
        "candidate": response.get("candidate"),
        "context": response.get("context"),
        "total_duration": response.get("total_duration"),
        "prompt_duration": response.get("prompt_duration"),
        "generate_duration": response.get("generate_duration"),
        "eval_duration": response.get("eval_duration"),
        "model_name": response.get("model_name"),
        "created_at": response.get("created_at"),
        "modified_at": response.get("modified_at"),
        "model_version": response.get("model_version"),
        "model_size": response.get("model_size"),
        "model_format": response.get("model_format")
    }

# Utility for parsing Ollama pull model response
def parse_pull_model_response(response: dict) -> dict:
    return {
        "status": response.get("status"),
        "name": response.get("name"),
        "description": response.get("description"),
        "modified_at": response.get("modified_at"),
        "size": response.get("size"),
        "quant,