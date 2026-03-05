class BibleEditor:
    def __init__(self, db):
        self.db = db

    def add_verse(self, book, chapter, verse, text):
        self.db.conn.execute("INSERT INTO verses (book, chapter, verse, text) VALUES (?, ?, ?, ?)", (book, chapter, verse, text))
        self.db.conn.commit()