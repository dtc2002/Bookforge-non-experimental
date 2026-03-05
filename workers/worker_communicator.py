import json
import sqlite3
from celery import Celery

# Initialize Celery
celery_app = Celery(
    "worker_communicator",
    broker="pyrabbitmq://guest:guest@localhost:5672/",
    backend="db+sqlite:///tasks.db"
)

# Connect to SQLite database
conn = sqlite3.connect("tasks.db")
conn.execute("""
CREATE TABLE IF NOT EXISTS task_status (
    task_id TEXT PRIMARY KEY,
    status TEXT,
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    result TEXT
);
""")
conn.commit()

# Task status tracking
@celery_app.task(name="worker.status.update")
def update_task_status(task_id, status, result):
    """Update task status in the database"""
    conn.execute("""
    UPDATE task_status
    SET status = ?, end_time = CURRENT_TIMESTAMP, result = ?
    WHERE task_id = ?
    """, (status, json.dumps(result), task_id))
    conn.commit()

# Result retrieval
@celery_app.task(name="worker.result.get")
def get_task_result(task_id):
    """Retrieve task result from the database"""
    cursor = conn.execute("""
    SELECT result FROM task_status WHERE task_id = ?
    """, (task_id,))
    result = cursor.fetchone()
    return json.loads(result[0]) if result else None