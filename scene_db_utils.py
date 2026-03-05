import sqlite3
from datetime import datetime

# Initialize SQLite database
def init_scene_db():
    conn = sqlite3.connect('scenes.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS scenes (
            scene_id INTEGER PRIMARY KEY AUTOINCREMENT,
            scene_number INTEGER NOT NULL,
            scene_goal TEXT NOT NULL,
            key_beats TEXT NOT NULL,
            dialogue_prompts TEXT NOT NULL,
            continuity_markers TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Save scene cards to database
def save_scene_cards(cards):
    conn = sqlite3.connect('scenes.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO scenes (scene_number, scene_goal, key_beats, dialogue_prompts, continuity_markers)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        cards['scene_number'],
        cards['scene_goal'],
        str(cards['key_beats']),
        str(cards['dialogue_prompts']),
        str(cards['continuity_markers'])
    ))
    conn.commit()
    conn.close()