class SerialPlanner:
    def __init__(self):
        self.chapters = []

    def plan_serial(self, topics):
        for topic in topics:
            self.chapters.append(self.create_chapter(topic))
        return self.chapters