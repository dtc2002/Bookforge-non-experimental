from sqlalchemy import create_engine, Column, String, Text, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.declarative import declared_base

Base = declared_base()

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    role = Column(String(255))
    traits = Column(Text)

class PlotThread(Base):
    __tablename__ = 'plot_threads'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    summary = Column(Text)
    key_events = Column(Text)

class CanonFact(Base):
    __tablename__ = 'canon_facts'
    id = Column(Integer, primary_key=True)
    statement = Column(Text, nullable=False)
    sources = Column(Text)

# Initialize database
engine = create_engine('sqlite:///literary_ai.db', echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# CRUD operations
def create_character(session, name: str, role: str = None, traits: Dict = None):
    character = Character(name=name, role=role, traits=str(traits) if traits else None)
    session.add(character)
    session.commit()
    session.refresh(character)
    return character

def get_characters(session):
    return session.query(Character).all()

# Add more CRUD functions for PlotThread and CanonFact as needed