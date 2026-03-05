import json

class ProjectSaver:
    def save_project(self, project):
        with open('project.json', 'w') as f:
            json.dump(project, f)