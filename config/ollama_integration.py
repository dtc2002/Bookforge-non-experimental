import os
import subprocess
from models import Model

def discover_ollama_models():
    try:
        # Check Ollama models directory
        models_dir = os.path.expanduser('~/ollama/models')
        if not os.path.exists(models_dir):
            os.makedirs(models_dir)

        # List available models
        result = subprocess.run([
            'ollama', 'list'
        ],
        capture_output=True,
        text=True,
        check=True
        )

        models = {}
        for line in result.stdout.splitlines()[1:]:
            model_info = line.split()
            model_id = model_info[0]
            model_name = model_info[1]
            model_type = model_info[2]
            models[model_id] = {
                'name': model_name,
                'type': model_type,
                'description': f"Ollama model {model_name} ({model_type})"
            }

        # Save to database
        for model_id, model_data in models.items():
            model = Model.query.get(model_id)
            if not model:
                model = Model(id=model_id, **model_data)
                Model.db.session.add(model)
            else:
                for key, value in model_data.items():
                    setattr(model, key, value)
        Model.db.session.commit()

        return models
    except Exception as e:
        print(f"Error discovering Ollama models: {str(e)}")
        return {}