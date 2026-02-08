from dataclasses import dataclass, field
from typing import List

@dataclass
class User:
    name: str
    # ПРАВИЛЬНЫЙ способ для изменяемых типов
    friends: List[str] = field(default_factory=list)