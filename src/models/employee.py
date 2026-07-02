"""
====================================================
VisionWork AI
Employee Model
====================================================
"""

from dataclasses import dataclass, field
from typing import Tuple, List
import time


@dataclass(slots=True)
class Employee:

    # Tracking
    track_id: int
    bbox: Tuple[int, int, int, int]
    confidence: float

    # Identity
    name: str = "Unknown"
    employee_id: str = ""
    department: str = "Unknown"

    # Status
    status: str = "Present"

    # Activity
    working: bool = False
    idle: bool = False
    phone_detected: bool = False
    laptop_detected: bool = False
    attention_score: float = 100.0

    # Time Statistics
    working_time: float = 0.0
    idle_time: float = 0.0

    first_seen: float = field(default_factory=time.time)
    last_seen: float = field(default_factory=time.time)

    # Desk Information
    desk_id: str = "Unknown"

    # Tracking History
    trajectory: List[Tuple[int, int]] = field(default_factory=list)
    missing: int = 0

    @property
    def center(self):

        x1, y1, x2, y2 = self.bbox

        return (
            (x1 + x2) // 2,
            (y1 + y2) // 2
        )

    def update_bbox(self, bbox):

        self.bbox = bbox

        self.last_seen = time.time()

        self.trajectory.append(self.center)

    def update_confidence(self, confidence):

        self.confidence = confidence

    def set_status(self, status):

        self.status = status

    def add_working_time(self, seconds):

        self.working_time += seconds

    def add_idle_time(self, seconds):

        self.idle_time += seconds

    def mark_phone(self, state: bool):

        self.phone_detected = state

    def mark_laptop(self, state: bool):

        self.laptop_detected = state

    def reset_attention(self):

        self.attention_score = 100.0

    def __repr__(self):

        return (
            f"Employee("
            f"id={self.track_id}, "
            f"status={self.status}, "
            f"confidence={self.confidence:.2f})"
        )