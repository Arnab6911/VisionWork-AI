"""
====================================================
VisionWork AI
Employee Model
====================================================
"""

from dataclasses import dataclass, field
from typing import Tuple, List


@dataclass
class Employee:

    track_id: int

    bbox: Tuple[int, int, int, int]

    confidence: float

    status: str = "Present"

    phone_detected: bool = False

    laptop_detected: bool = False

    attention_score: float = 100.0

    idle_time: float = 0.0

    working_time: float = 0.0

    desk_id: str = "Unknown"

    trajectory: List[Tuple[int, int]] = field(default_factory=list)

    def center(self):

        x1, y1, x2, y2 = self.bbox

        return ((x1 + x2)//2, (y1 + y2)//2)

    def update_bbox(self, bbox):

        self.bbox = bbox

        self.trajectory.append(self.center())

    def __str__(self):

        return f"Employee {self.track_id}"