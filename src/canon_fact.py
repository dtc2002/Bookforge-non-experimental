from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass
class CanonFact:
    id: str
    thread: str
    fact: str
    created_at: datetime
    last_modified: datetime
    
    def to_dict(self):
        return {
            "id": self.id,
            "thread": self.thread,
            "fact": self.fact,
            "created_at": self.created_at.isoformat(),
            "last_modified": self.last_modified.isoformat()
        }