from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass
class PlotThread:
    id: str
    universe: str
    title: str
    description: str
    created_at: datetime
    last_modified: datetime
    
    def to_dict(self):
        return {
            "id": self.id,
            "universe": self.universe,
            "title": self.title,
            "description": self.description,
            "created_at": self.created_at.isoformat(),
            "last_modified": self.last_modified.isoformat()
        }