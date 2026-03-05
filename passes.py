def generate_scene_cards(story_context, current_scene):
    """
    Generate scene cards using Ollama model
    Args:
        story_context (str): Context about the story
        current_scene (str): Current scene details
    Returns:
        dict: Scene cards with goals, beats, dialogue, and continuity
    """
    # Select Ollama model (default to llama3)
    model = "llama3"

    # Prepare prompt for scene generation
    prompt = f"""
    Story Context:
    {story_context}

    Current Scene:
    {current_scene}

    Please generate scene cards with:
    1. Scene goal
    2. Key beats
    3. Dialogue prompts
    4. Continuity markers
    """

    # Call Ollama API (mock implementation)
    response = {
        "scene_goal": "The protagonist discovers a hidden message in the library",
        "key_beats": [
            "Protagonist enters dusty library",
            "Finds encrypted book",
            "Deciphers message revealing secret society",
            "Decides to investigate further"
        ],
        "dialogue_prompts": [
            "'I've always suspected there was more to this place,' says the librarian.",
            "'This message is a warning about the society's experiments.'"
        ],
        "continuity_markers": [
            "Library discovery connects to previous chapter's mystery",
            "Secret society setup for future plot twists"
        ]
    }

    return response