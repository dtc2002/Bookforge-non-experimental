from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass
class UniverseBible:
    id: str
    project: str
    version: str
    created_at: datetime
    last_modified: datetime
    
    def to_dict(self):
        return {
            "id": self.id,
            "project": self.project,
            "version": self.version,
            "created_at": self.created_at.isoformat(),
            "last_modified": self.last_modified.isoformat()
        }