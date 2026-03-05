# storage/project_saver.py
import json

class ProjectSaver:
    def __init__(self, save_path='project_state.json'):
        self.save_path = save_path

    def save_project(self, data):
        with open(self.save, 'w') as f:
            json.dump(data, f)

    def load_project(self):
        with open(self.save, 'r') as f:
            return json.load(f)
