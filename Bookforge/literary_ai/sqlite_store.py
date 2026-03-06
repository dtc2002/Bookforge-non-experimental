import sqlite3
from typing import List, Dict, Any
from .schemas import ArtifactSchema

class SQLiteStore:
    def __init__(self, db_path: str = "./bookforge.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        """Initialize the database schema"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('CREATE TABLE IF NOT EXISTS artifacts (id TEXT PRIMARY KEY, content TEXT, metadata JSON, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP)')
            conn.execute('CREATE TABLE IF NOT EXISTS chapters (id TEXT PRIMARY KEY, book_id TEXT, chapter_number INTEGER, title TEXT, content TEXT, FOREIGN KEY(book_id) REFERENCES artifacts(id))')
            conn.execute('CREATE TABLE IF NOT EXISTS books (id TEXT PRIMARY KEY, title TEXT, author TEXT, cover_art TEXT, publication_date TIMESTAMP)')

    def save_artifact(self, artifact: ArtifactSchema) -> str:
        """Save an artifact to the database"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO artifacts (id, content, metadata, created_at, updated_at) VALUES (?, ?, ?, ?, ?)',
                           (artifact.id, artifact.content, json.dumps(artifact.metadata), artifact.created_at, artifact.updated_at))
            return cursor.lastrowid

    def get_artifact(self, artifact_id: str) -> Dict[str, Any]:
        """Get an artifact by ID"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM artifacts WHERE id = ?', (artifact_id,))
            row = cursor.fetchone()
            if row:
                return {
                    'id': row[0],
                    'content': row[1],
                    'metadata': json.loads(row[2]),
                    'created_at': row[3],
                    'updated_at': row[4]
                }
            return None

    def list_artifacts(self) -> List[Dict[str, Any]]:
        """List all artifacts"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM artifacts')
            rows = cursor.fetchall()
            return [{
                'id': row[0],
                'content': row[1],
                'metadata': json.loads(row[2]),
                'created_at': row[3],
                'updated_at': row[4]
            } for row in rows]
