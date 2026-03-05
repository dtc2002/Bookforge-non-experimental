import click
from passes import generate_chapter_briefs
from orchestrator import run_pass_3
from checkers import check_character_consistency
from pacing import validate_conflict_escalation

@click.group()
def cli():
    """Literary AI CLI tool"""
    pass

@cli.command()
@click.argument('story_summary')
def briefs(story_summary):
    """Generate chapter briefs for a story"""
    try:
        # Run Pass 3
        chapter_briefs = run_pass_3(story_summary)
        
        # Validate consistency
        check_character_consistency(chapter_briefs)
        validate_conflict_peated_escalation(chapter_briefs)
        
        # Output results
        click.echo("Chapter briefs generated successfully!"
    except Exception as e:
        click.echo(f"Error generating briefs: {str(e)}", err=True)
        exit(1)