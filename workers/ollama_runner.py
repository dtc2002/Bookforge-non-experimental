import subprocess
import os
from models import Model

def run_ollama_model(model_id):
    model = Model.query.get(model_id)
    if not model:
        raise ValueError(f"Model {model_id} not found")

    # Check if Ollama is installed
    if not os.path.exists('/usr/local/bin/ollama'):
        raise RuntimeError("Ollama not found in PATH")

    # Run the model
    result = subprocess.run([
        'ollama', 'run',
        model.name,
        '--model', model.type
    ],
    capture_output=True,
    text=True,
    check=True
    )

    return result.stdout