## Literary AI Project

### Structure
- gui/ (main_window.py, settings.py)
- llm_integration/ (llm_connector.py, prompt_engine.py)
- universe_bible/ (bible_db.py, bible_editor.py)
- content_generator/ (chapter_creator.py, serial_planner.py)
- storage/ (project_saver.py, bible_saver.py)
- main.py

### Setup
1. Create venv: `python -m venv venv`
2. Install dependencies: `venv/bin/pip install -r requirements.txt`

### Requirements.txt
```
tkinter
transformers
sqlite3
```

### Usage
Run `main.py` to start the application.