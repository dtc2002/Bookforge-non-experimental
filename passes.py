def generate_chapter_briefs(story_summary, chapter_count):
    """Generate chapter briefs using Ollama model"""
    import orjson
    import requests
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ.get('OLLAMA_API_KEY')}",
    }
    
    briefs = []
    for chapter in range(1, chapter_count + 1):
        payload = {
            "model": "llama3",
            "prompt": f"Story Summary: {story_summary}\n\nGenerate chapter {chapter} brief with these elements:\n1. Primary goal\n2. Core conflict\n3. Key outcome\n4. Scene breakdown (3-5 scenes)\n5. Character motivations\n6. Continuity dependencies\n\nRespond in JSON format with these keys: goals, conflict, outcomes, scenes, motivations, continuity_dependencies",
            "stream": False,
        }
        
        response = requests.post("http://localhost:11434/api/generate", headers=headers, json=payload)
        response_data = response.json()
        
        # Extract JSON from response
        try:
            chapter_data = orjson.loads(response_data["response"])
        except:
            chapter_data = {
                "goals": [],
                "conflict": "",
                "outcomes": [],
                "scenes": [],
                "motivations": {},
                "continuity_dependencies": [],
            }
        
        briefs.append(chapter_data)
    
    return briefs