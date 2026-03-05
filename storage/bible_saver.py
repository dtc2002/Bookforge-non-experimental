import sqlite3

class BibleSaver:
    def save_bible(self, bible):
        conn = sqlite3.connect('bible.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM verses')
        for book, chapters in bible.items():
            for chapter, verses in chapters.items():
                for verse, text in verses.items():
                    cursor.execute("INSERT INTO verses (book, chapter, verse, text) VALUES (?, ?, ?, ?)", (book, chapter, verse, text))
        conn.commit()
        conn.close()