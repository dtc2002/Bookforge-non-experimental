import sqlite3
from typing import List, Dict, Any

# Initialize draft storage
conn = sqlite3.connect('drafts.db', check_same_thread=False)
conn.execute('CREATE TABLE IF NOT EXISTS scene_drafts (id INTEGER PRIMARY KEY AUTOINCREMENT, scene_number INTEGER, timestamp TEXT, content TEXT, characters TEXT)')
conn.commit()

def save_drafts(drafts: List[Dict[str, Any]]) -> None:
    """
    Save scene drafts to SQLite database
    """
    cursor = conn.cursor()
    cursor.execute('DELETE FROM scene_drafts')  # Clear previous drafts
    cursor.executemany('INSERT INTO scene_drafts (scene_number, timestamp, content, characters) VALUES (?, ?, ?, ?)',
                      [(d['scene_number'], d['timestamp'], d['content'], ', '.join(d['characters'])) for d in drafts])
    conn.commit()

# Add to orchestrator workflow
# Orchestrator will handle repair loops and integration with checker systems