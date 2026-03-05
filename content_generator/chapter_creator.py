# content_generator/chapter_creator.py
from .bible_db import BibleDB
from .llm_connector import LLMBridge

class ChapterCreator:
    def __init__(self, bible, llm):
        self.bible = bible
        self.llm = llm

    def generate_chapter(self, concept):
        context = self.bible.get_entries()
        prompt = self.llm.create_prompt(context)
        return self.llm.generate(prompt)

# content_generator/serial_planner.py
from .bible_db import BibleDB

class SerialPlanner:
    def __init__(self, bible):
        self.bible = bible

    def plan_serial(self):
        # Logic to plan serialization based on bible entries
        return 'Serialization plan generated'
