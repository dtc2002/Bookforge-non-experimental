class Shortcuts:
    def __init__(self, app):
        self.app = app
        self.shortcuts = {
            "Ctrl+S": "save",
            "Ctrl+Z": "undo",
            "Ctrl+Y": "redo",
            "Ctrl+E": "export"
        }

    def register(self):
        for key, action in self.shortcuts.items():
            self.app.register_shortcut(key, action)