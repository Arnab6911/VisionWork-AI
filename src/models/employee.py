"""
====================================================
VisionWork AI
Employee Model
====================================================
"""

from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass(slots=True)
class Employee:

    track_id: int

    bbox: Tuple[int, int, int, int]

    confidence: float

    status: str = "Present"

    desk: str = "Unknown"

    attention_score: float = 100.0

    idle_time: float = 0.0

    working_time: float = 0.0

    phone_detected: bool = False

    laptop_detected: bool = False

    trajectory: List[Tuple[int, int]] = field(default_factory=list)

    def update_bbox(self, bbox):

        self.bbox = bbox

        self.trajectory.append(self.center)

    @property
    def center(self):

        x1, y1, x2, y2 = self.bbox

        return (

            (x1 + x2) // 2,

            (y1 + y2) // 2,

        )

    def reset_idle(self):

        self.idle_time = 0

    def add_idle(self, seconds):

        self.idle_time += seconds

    def add_work(self, seconds):

        self.working_time += seconds