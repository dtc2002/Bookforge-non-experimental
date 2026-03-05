import click
from celery import Celery

# Initialize Celery
celery_app = Celery(
    "scheduler",
    broker="pyrabbitmq://guest:guest@localhost:5672/",
    backend="db+sqlite:///tasks.db"
)

@click.command()
@click.option("--priority", type=click.IntRange(0, 10), default=5)
def start_worker(priority):
    """Start a worker with specified task priority"""
    celery_app.conf.task_default_queue = f"priority_{priority}"
    celery_app.start()

if __name__ == "__main__":
    start_worker()