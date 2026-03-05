def run_pass_3(story_summary):
    """Execute Pass 3: Chapter Briefs Generation"""
    from passes import generate_chapter_briefs
    import sqlite3
    
    # Generate chapter briefs
    chapter_briefs = generate_chapter_briefs(story_summary, 10)  # Assume 10 chapters
    
    # Store in SQLite
    conn = sqlite3.connect('story_db.sqlite')
    cursor = conn.cursor()
    
    # Create table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS chapter_briefs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chapter_number INTEGER,
            goals TEXT,
            conflict TEXT,
            outcomes TEXT,
            scenes TEXT,
            motivations TEXT,
            continuity_dependencies TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Insert data
    for brief in chapter_briefs:
        cursor.execute('''
            INSERT INTO chapter_briefs (
                chapter_number,
                goals,
                conflict,
                outcomes,
                scenes,
                motivations,
                continuity_dependencies
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            brief.get('chapter_number', 0),
            orjson.dumps(brief.get('goals', [])),
            brief.get('conflict', ''),
            orjson.dumps(brief.get('outcomes', [])),
            orjson.dumps(brief.get('scenes', [])),
            orjson.dumps(brief.get('motivations', {})),
            orjson.dumps(brief.get('continuity_dependencies', []))
        ))
    
    conn.commit()
    conn.close()
    
    # Run repair loop
    from repair import check_for_inconsistencies
    check_for_inconsistencies()
    
    return chapter_briefs