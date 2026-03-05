def validate_conflict_escalation(chapter_briefs):
    """Validate conflict escalation across chapters"""
    from sqlite3 import connect
    
    # Check if conflict escalates appropriately
    current_conflict = None
    for brief in chapter_briefs:
        conflict = brief.get('conflict', '')
        if current_conflict is None:
            current_conflict = conflict
        elif conflict.strip() == current_conflict.strip():
            raise ValueError(f"Conflict stagnation detected in chapter {brief['chapter_number']}")
        current_conflict = conflict
    
    # Check for resolution in final chapter
    final_chapter = max(brief['chapter_number'] for brief in chapter_briefs)
    final_conflict = next(brief['conflict'] for brief in chapter_briefs if brief['chapter_number'] == final_chapter)
    if final_conflict.strip() == "":
        raise ValueError("Final chapter conflict resolution missing")
    
    return True