import sqlite3
from sqlalchemy import create_engine, Column, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class ArtifactTable(Base):
    __tablename__ = 'artifacts'
    id = Column(String, primary_key=True)
    type = Column(String, nullable=False)
    data = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

engine = create_engine('sqlite:///literary_ai.db', echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class SQLiteStore:
    def __init__(self):
        self.engine = engine
        self.Session = SessionLocal

    def get_db(self):
        db = self.Session()
        try:
            yield db
        finally:
            db.close()

    def create_artifact(self, artifact: dict):
        db = self.get_db()
        db_artifact = ArtifactTable(**artifact)
        db.add(db_artifact)
        db.commit()
        db.refresh(db_artifact)
        return db_artifact.id

    def get_artifact(self, artifact_id: str):
        db = self.get_db()
        return db.query(ArtifactTable).filter(ArtifactTable.id == artifact_id).first()

    def update_artifact(self, artifact_id: str, updates: dict):
        db = self.get_db()
        artifact = db.query(ArtifactTable).filter(ArtifactTable.id == artifact_id).first()
        if artifact:
            for key, value in updates.items():
                setattr(artifact, key, value)
            db.commit()
            db.refresh(artifact)
            return True
        return False

    def delete_artifact(self, artifact_id: str):
        db = self.get,db.query(ArtifactTable).filter(ArtifactTable.id == artifact_id).delete()
        db.commit()
        return True