import sqlite3
from datetime import datetime
from typing import List, Dict, Optional

class SQLiteStore:
    def __init__(self, db_path: str = "./data.db"):
        self.db_path = db_path
        self.init_db()

    def init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS characters (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    description TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.execute('''
                CREATE TABLE IF NOT EXISTS plot_threads (
                    id TEXT PRIMARY KEY,
                    universe TEXT NOT NULL,
                    title TEXT NOT NULL,
                    description TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.execute('''
                CREATE TABLE IF NOT EXISTS canon_facts (
                    id TEXT PRIMARY KEY,
                    thread_id TEXT NOT NULL,
                    fact TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')

    def get_all_characters(self) -> List[Dict]:
        with sqlite3.connect(self.db_path) as conn:
            return conn.execute("SELECT * FROM characters").fetchall()

    def get_all_plot_threads(self) -> List[Dict]:
        with sqlite3.connect(self.db_path) as conn:
            return conn.execute("SELECT * FROM plot_threads").fetchall()

    def get_all_canon_facts(self) -> List[Dict]:
        with sqlite3.connect(self.db_path) as conn:
            return conn.execute("SELECT * FROM canon_facts").fetchall()

    def add_character(self, name: str, description: Optional[str] = None) -> str:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("INSERT INTO characters (name, description) VALUES (?, ?)", (name, description))
            return cursor.lastrowid

    def add_plot_thread(self, universe: str, title: str, description: Optional[str] = None) -> str:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("INSERT INTO plot_threads (universe, title, description) VALUES (?, ?, ?)", (universe, title, description))
            return cursor.lastrowid

    def add_canon_fact(self, thread_id: str, fact: str) -> str:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("INSERT INTO canon_facts (thread_id, fact) VALUES (?, ?)", (thread_id, fact))
            return cursor.lastrowid