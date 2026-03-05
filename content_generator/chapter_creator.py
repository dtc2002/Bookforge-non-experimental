class ChapterCreator:
    def __init__(self, llm_connector):
        self.llm_connector = llm_connector

    def create_chapter(self, topic):
        prompt = self.llm_connector.generate_text(self.llm_connector.prompt_engine.create_prompt(topic))
        return prompt