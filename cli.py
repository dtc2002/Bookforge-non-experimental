import click

@click.command()
@click.option('--story', required=True, help='Story context for scene generation')
def generate_scenes(story):
    """
    CLI command for generating literary scenes
    """
    # Generate scene cards
    scene_cards = generate_scene_cards(
        story_context=story,
        current_scene=""
    )

    # Print results
    click.echo("Generated Scene Cards:")
    click.echo(f"Goal: {scene_cards['scene_goal']}")
    click.echo("Key Beats:")
    for beat in scene_cards['key_beats']:
        click.echo(f"- {beat}")
    click.echo("Dialogue Prompts:")
    for dialogue in scene_cards['dialogue_prompts']:
        click.echo(f"- {dialogue}")
    click.echo("Continuity Markers:")
    for marker in scene_cards['continuity_markers']:
        click.echo(f"- {marker}")