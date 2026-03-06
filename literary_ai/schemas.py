from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import datetime
from uuid import UUID
from rich.progress import Progress, TaskDescription
from contextlib import asynccontextmanager
from contextvars import ContextVar
from urllib.parse import urlparse

# Base model for all configurations
class ProjectConfig(BaseModel):
    model_name: str = "llama3"
    temperature: float = 0.7
    max_tokens: int = 512
    stream: bool = False
    stop_sequences: List[str] = Field(default_factory=list)
    prompt_prefix: str = ""
    response_suffix: str = ""
    model_kwargs: Dict[str, any] = Field(default_factory=dict)

    class Config:
        arbitrary_types_allowed = True

# Universe Bible structure
class UniverseBible(BaseModel):
    name: str
    description: str
    entities: List[Dict[str, any]] = Field(default_factory=list)
    rules: Dict[str, str] = Field(default_factory=dict)
    canonical_facts: List[Dict[str, any]] = Field(default_factory=list)
    
    class Config:
        arbitrary_types_allowed = True

# Story artifacts
class StoryArtifact(BaseModel):
    type: str
    content: str
    metadata: Dict[str, any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    modified_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        arbitrary_types_allowed = True

# Checker findings
class CheckerFinding(BaseModel):
    category: str
    detail: str
    severity: str = "info"
    suggestion: Optional[str] = None
    location: Dict[str, any] = Field(default_factory=dict)

    class Config:
        arbitrary_types_allowed = True

# Database models
class Character(BaseModel):
    id: UUID
    name: str
    role: str
    background: str
    relationships: Dict[str, str] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    modified_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        arbitrary_types_allowed = True

class PlotThread(BaseModel):
    id: UUID
    title: str
    summary: str
    key_events: List[str] = Field(default_factory=list)
    connections: Dict[str, str] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    modified_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        arbitrary_types_allowed = True

class CanonFact(BaseModel):
    id: UUID
    statement: str
    justification: str
    references: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    modified_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        arbitrary_types_allowed = True

# Database operations
class Database(BaseModel):
    db_path: str = "/data/literary_ai.db"
    
    def __init__(self, db_path: str = "/data/literary_ai.db"):  # noqa: E731
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        import sqlite3
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS characters (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                role TEXT NOT NULL,
                background TEXT NOT NULL,
                relationships TEXT NOT NULL DEFAULT '{}',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )""")
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS plot_threads (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                summary TEXT NOT NULL,
                key_events TEXT NOT NULL DEFAULT '[]',
                connections TEXT NOT NULL DEFAULT '{}',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )""")
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS canon_facts (
                id TEXT PRIMARY KEY,
                statement TEXT NOT NULL,
                justification TEXT NOT NULL,
                references TEXT NOT NULL DEFAULT '[]',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )""")
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS story_artifacts (
                id TEXT PRIMARY KEY,
                type TEXT NOT NULL,
                content TEXT NOT NULL,
                metadata TEXT NOT NULL DEFAULT '{}',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )""")
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS checker_findings (
                id TEXT PRIMARY KEY,
                category TEXT NOT NULL,
                detail TEXT NOT NULL,
                severity TEXT NOT NULL,
                suggestion TEXT,
                location TEXT NOT NULL DEFAULT '{}',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )""")

    def close(self):
        self.conn.close()

    def _execute(self, query, params=None):
        cursor = self.conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        return cursor

    def _fetchall(self, cursor):
        return cursor.fetchall()

    def _fetchone(self, cursor):
        return cursor.fetchone()

    def _commit(self):
        self.conn.commit()

    def _update_modified_at(self):
        self.conn.execute("""
            UPDATE characters
            SET modified_at = CURRENT_TIMESTAMP
            WHERE id = ?
            """, [self._get_id()])
        self.conn.execute("""
            UPDATE plot_threads
            SET modified_at = CURRENT_TIMESTAMP
            WHERE id = ?
            """, [self._get_id()])
        self.conn.execute("""
            UPDATE canon_facts
            SET modified_at = CURRENT_TIMESTAMP
            WHERE id = ?
            """, [self._get_id()])
        self.conn.execute("""
            UPDATE story_artifacts
            SET modified_at = CURRENT_TIMESTAMP
            WHERE id = ?
            """, [self._get_id()])
        self.conn.execute("""
            UPDATE checker_findings
            SET modified_at = CURRENT_TIMESTAMP
            WHERE id = ?
            """, [self._get, self._get_id()])
        self.conn.commit()

    def _get_id(self):
        return self.id

    # Character operations
    def add_character(self, character: Character):
        self._execute("""
            INSERT INTO characters (id, name, role, background, relationships)
            VALUES (?, ?, ?, ?, ?)
            """,
            (character.id, character.name, character.role, character.background, character.relationships))
        self._update_modified_at()
        self._commit()
        return self._get_character(character.id)

    def _get_character(self, character_id: str):
        cursor = self._execute("""
            SELECT * FROM characters WHERE id = ?
            """,
            (character_id,))
        result = self._fetchone(cursor)
        if result:
            return Character(
                id=result[0],
                name=result[1],
                role=result[2],
                background=result[3],
                relationships=eval(result[4])
            )
        return None

    def update_character(self, character: Character):
        self._execute("""
            UPDATE characters
            SET name = ?, role = ?, background = ?, relationships = ?
            WHERE id = ?
            """,
            (character.name, character.role, character.background, str(character.relationships), character.id))
        self._update_modified_at()
        self._commit()
        return self._get_character(character.id)

    def delete_character(self, character_id: str):
        self._execute("""
            DELETE FROM characters WHERE id = ?
            """,
            (character_id,))
        self._commit()
        return True

    def get_all_characters(self):
        cursor = self._execute("""
            SELECT * FROM characters
            """)
        results = self._fetchall(cursor)
        return [Character(
            id=result[0],
            name=result[1],
            role=result[2],
            background=result[3],
            relationships=eval(result[4])
        ) for result in results]

    # Plot Thread operations
    def add_plot_thread(self, plot_thread: PlotThread):
        self._execute("""
            INSERT INTO plot_threads (id, title, summary, key_events, connections)
            VALUES (?, ?, ?, ?, ?)
            """,
            (plot_thread.id, plot_thread.title, plot_thread.summary, str(plot_thread.key_events), plot_thread.connections))
        self._update_modified_at()
        self._commit()
        return self._get_plot_thread(plot_thread.id)

    def _get_plot_thread(self, plot_thread_id: str):
        cursor = self._execute("""
            SELECT * FROM plot_threads WHERE id = ?
            """,
            (plot_thread_id,))
        result = self._fetchone(cursor)
        if result:
            return PlotThread(
                id=result[0],
                title=result[1],
                summary=result[2],
                key_events=eval(result[3]),
                connections=eval(result[4])
            )
        return None

    def update_plot_thread(self, plot_thread: PlotThread):
        self._execute("""
            UPDATE plot_threads
            SET title = ?, summary = ?, key_events = ?, connections = ?
            WHERE id = ?
            """,
            (plot_thread.title, plot_thread.summary, str(plot_thread.key_events), str(plot_thread.connections), plot_thread.id))
        self._update_modified_at()
        self._commit()
        return self._get_plot_thread(plot_thread.id)

    def delete_plot_thread(self, plot_thread_id: str):
        self._execute("""
            DELETE FROM plot_threads WHERE id = ?
            """,
            (plot_thread_id,))
        self._commit()
        return True

    def get_all_plot_threads(self):
        cursor = self._execute("""
            SELECT * FROM plot_threads
            """)
        results = self._fetchall(cursor)
        return [PlotThread(
            id=result[0],
            title=result[1],
            summary=result[2],
            key_events=eval(result[3]),
            connections=eval(result[4])
        ) for result in results]

    # Canon Fact operations
    def add_canon_fact(self, canon_fact: CanonFact):
        self._execute("""
            INSERT INTO canon_facts (id, statement, justification, references)
            VALUES (?, ?, ?, ?)
            """,
            (canon_fact.id, canon_fact.statement, canon_fact.justification, str(canon_fact.references)))
        self._update_modified_at()
        self._commit()
        return self._get_canon_fact(canon_fact.id)

    def _get_canon_fact(self, canon_fact_id: str):
        cursor = self._execute("""
            SELECT * FROM canon_facts WHERE id = ?
            """,
            (canon_fact_id,))
        result = self._fetchone(cursor)
        if result:
            return CanonFact(
                id=result[0],
                statement=result[1],
                justification=result[2],
                references=eval(result[3])
            )
        return None

    def update_canon_fact(self, canon_fact: CanonFact):
        self._execute("""
            UPDATE canon_facts
            SET statement = ?, justification = ?, references = ?
            WHERE id = ?
            """,
            (canon_fact.statement, canon_fact.justification, str(canon_fact.references), canon_fact.id))
        self._update_modified_at()
        self._commit()
        return self._get_canon_fact(canon_fact.id)

    def delete_canon_fact(self, canon_fact_id: str):
        self._execute("""
            DELETE FROM canon_facts WHERE id = ?
            """,
            (canon_fact_id,))
        self._commit()
        return True

    def get_all_canon_facts(self):
        cursor = self._execute("""
            SELECT * FROM canon_facts
            """)
        results = self._fetchall(cursor)
        return [CanonFact(
            id=result[0],
            statement=result[1],
            justification=result[2],
            references=eval(result[3])
        ) for result in results]

    # Story Artifact operations
    def add_story_artifact(self, story_artifact: StoryArtifact):
        self._execute("""
            INSERT INTO story_artifacts (id, type, content, metadata)
            VALUES (?, ?, ?, ?)
            """,
            (story_artifact.id, story_artifact.type, story_artifact.content, str(story_artifact.metadata)))
        self._update_modified_at()
        self._commit()
        return self._get_story_artifact(story_artifact.id)

    def _get_story_artifact(self, story_artifact_id: str):
        cursor = self._execute("""
            SELECT * FROM story_artifacts WHERE id = ?
            """,
            (story_artifact_id,))
        result = self._fetchone(cursor)
        if result:
            return StoryArtifact(
                id=result[0],
                type=result[1],
                content=result[2],
                metadata=eval(result[3])
            )
        return None

    def update_story_artifact(self, story_artifact: StoryArtifact):
        self._execute("""
            UPDATE story_artifacts
            SET type = ?, content = ?, metadata = ?
            WHERE id = ?
            """,
            (story_artifact.type, story_artifact.content, str(story_artifact.metadata), story_artifact.id))
        self._update_modified, story_artifact.id))
        self._commit()
        return self._get_story_artifact(story_artifact.id)

    def delete_story_artifact(self, story_artifact_id: str):
        self._execute("""
            DELETE FROM story_artifacts WHERE id = ?
            """,
            (story_artifact_id,))
        self._commit()
        return True

    def get_all_story_artifacts(self):
        cursor = self._execute("""
            SELECT * FROM story_artifacts
            """)
        results = self._fetchall(cursor)
        return [StoryArtifact(
            id=result[0],
            type=result[1],
            content=result[2],
            metadata=eval(result[3])
        ) for result in results]

    # Checker Finding operations
    def add_checker_finding(self, checker_finding: CheckerFinding):
        self._execute("""
            INSERT INTO checker_findings (id, category, detail, severity, suggestion, location)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (checker_finding.id, checker_finding.category, checker_finding.detail, checker_finding.severity, checker_finding.suggestion, str(checker_finding.location)))
        self._update_modified_at()
        self._commit()
        return self._get_checker_finding(checker_finding.id)

    def _get_checker_finding(self, checker_finding_id: str):
        cursor = self._execute("""
            SELECT * FROM checker_findings WHERE id = ?
            """,
            (checker_finding_id,))
        result = self._fetchone(cursor)
        if result:
            return CheckerFinding(
                id=result[0],
                category=result[1],
                detail=result[2],
                severity=result[3],
                suggestion=result[4],
                location=eval(result[5])
            )
        return None

    def update_checker_finding(self, checker_finding: CheckerFinding):
        self._execute("""
            UPDATE checker_findings
            SET category = ?, detail = ?, severity = ?, suggestion = ?, location = ?
            WHERE id = ?
            """,
            (checker_finding.category, checker_finding.detail, checker_finding.severity, checker_finding.suggestion, str(checker_finding.location), checker_finding.id))
        self._update_modified_at()
        self._commit()
        return self._get_checker_finding(checker_finding.id)

    def delete_checker_finding(self, checker_finding_id: str):
        self._execute("""
            DELETE FROM checker_findings WHERE id = ?
            """,
            (checker_finding_id,))
        self._commit()
        return True

    def get_all_checker_findings(self):
        cursor = self._execute("""
            SELECT * FROM checker_findings
            """)
        results = self._fetchall(cursor)
        return [CheckerFinding(
            id=result[0],
            category=result[1],
            detail=result[2],
            severity=result[3],
            suggestion=result[4],
            location=eval(result[5])
        ) for result in results]

    # Utility methods
    def get_all(self):
        return {
            "characters": self.get_all_characters(),
            "plot_threads": self.get_all_plot_threads(),
            "canon_facts": self.get_all_canon_facts(),
            "story_artifacts": self.get_all_story_artifacts(),
            "checker_findings": self.get_all_checker_findings()
        }

    # Advanced operations
    def search(self, query: str):
        """Search all tables for matching records."""
        results = []
        for table in ["characters", "plot_threads", "canon_facts", "story_artifacts", "checker_findings"]:
            cursor = self._execute(f"""
                SELECT * FROM {table} WHERE name LIKE ? OR statement LIKE ? OR detail LIKE ?
                """, (f"%{query}%", f"%{query}%", f"%{query}%"))
            results.extend(self._fetchall(cursor))
        return results

    def export(self, file_path: str):
        """Export all data to a file."""
        with open(file_path, "w") as f:
            f.write(str(self.get_all()))
        return True

    def import_data(self, file_path: str):
        """Import data from a file."""
        with open(file_path, "r") as f:
            data = eval(f.read())
        for character in data.get("characters", []):
            self.add_character(character)
        for plot_thread in data.get("plot_threads", []):
            self.add_plot_thread(plot_thread)
        for canon_fact in data.get("canon_facts", []):
            self.add_canon_fact(canon_fact)
        for story_artifact in data.get("story_artifacts", []):
            self.add_story_artifact(story_artifact)
        for checker_finding in data.get("checker_findings", []):
            self.add_checker_finding(checker_finding)
        return True

    def __del__(self):
        self.close()

# Dependency injection for database
class DatabaseFactory:
    @staticmethod
    def create_database(db_path: str = "/data/literary_ai.db") -> Database:
        return Database(db_path)