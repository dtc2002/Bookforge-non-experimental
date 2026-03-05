-- SQLite Schema Enhancement
CREATE TABLE IF NOT EXISTS distributed_tasks (
    task_id TEXT PRIMARY KEY,
    queue_name TEXT NOT NULL,
    worker_id TEXT,
    status TEXT DEFAULT 'pending',
    priority INTEGER DEFAULT 5,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    started_at TIMESTAMP,
    completed_at TIMESTAMP,
    result TEXT,
    metadata JSON
);

-- Add indexes for performance
CREATE INDEX IF NOT EXISTS idx_queue_name ON distributed_tasks(queue_name);
CREATE INDEX IF NOT EXISTS idx_status ON distributed_tasks(status);