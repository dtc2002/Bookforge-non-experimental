import sqlite3

class BibleDB:
    def __init__(self):
        self.conn = sqlite3.connect('bible.db')
        self.create_table()

    def create_table(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS verses
                             (id INTEGER PRIMARY KEY, book TEXT, chapter INTEGER, verse INTEGER, text TEXT)''')