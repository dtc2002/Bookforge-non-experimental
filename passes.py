def finalize_drafts(draft):
    """Convert draft to export-ready format and save to SQLite"""
    
    # Format content with metadata
    formatted_content = f"""
### Scene Draft

**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

{draft}
"""
    
    # Save to SQLite database
    conn = sqlite3.connect('literary_ai.db')
    cursor = conn.cursor()
    
    # Create table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS drafts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT,
            format_type TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        INSERT INTO drafts (content, format_type)
        VALUES (?, ?)
    ''', (formatted_content, 'final'))
    
    conn.commit()
    conn.close()
    
    return {'status': 'success', 'message': 'Draft finalized and saved'}

# Example usage
if __name__ == '__main__':
    sample_draft = "A sample scene draft content..."
    result = finalize_drafts(sample_draft)
    print(result['message'])