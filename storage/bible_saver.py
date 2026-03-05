# storage/bible_saver.py
import json

class BibleSaver:
    def __init__(self, save_path='bible_state.json'):
        self.save_path = save_path

    def save_bible(self, data):
        with open(self.save_path, 'w') as f:
            json.dump(data, f)

    def load_bible(self):
        with open(self.save_path, 'r') as f:
            return json.load(f)
