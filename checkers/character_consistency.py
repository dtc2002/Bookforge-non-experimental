def check_character_consistency(chapter_briefs):
    """Check character consistency across chapter briefs"""
    from collections import defaultdict
    import sqlite3
    
    # Build character motivation map
    character_motivations = defaultdict(dict)
    for brief in chapter_briefs:
        for character, motivation in brief.get('motivations', {}).items():
            character_motivations[character][brief['chapter_number']] = motivation
    
    # Check consistency
    inconsistencies = []
    for character, chapters in character_motivations.items():
        previous_motivation = None
        for chapter_num, motivation in sorted(chapters.items()):
            if previous_motivation is not None and motivation != previous_motivation:
                inconsistencies.append({
                    "character": character,
                    "chapter": chapter_num,
                    "expected": previous_motivation,
                    "actual": motivation
                })
            previous_motivation = motivation
    
    if inconsistencies:
        raise ValueError(f"Found {len(inconsistencies)} character motivation inconsistencies")
    
    return True