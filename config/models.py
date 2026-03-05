from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class ModelAssignment(Base):
    __tablename__ = 'model_assignments'
    id = Column(Integer, primary_key=True)
    task_level = Column(String, nullable=False)
    model_id = Column(Integer, ForeignKey('models.id'), nullable=False)
    priority = Column(Integer, default=0)

    model = relationship("Model", back_populates="assignments")

class Model(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    description = Column(String)

    assignments = relationship("ModelAssignment", order_by=ModelAssignment.priority, back_populates="model")