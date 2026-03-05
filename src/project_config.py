from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass
class ProjectConfig:
    name: str
    description: str
    created_at: datetime = datetime.now()
    last_modified: datetime = datetime.now()
    
    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "created_at": self.created_at.isoformat(),
            "last_modified": self.last_modified.isoformat()
        }