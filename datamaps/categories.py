from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional


@dataclass_json
@dataclass
class MarkerCategory:
    name: Optional[str] = None
    subtleText: Optional[str] = None
    overrideIcon: Optional[str] = None
