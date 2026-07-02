'''track_state.py

Stores

Track ID

Age

Lost

Visible

History

Not Employee.

Only tracking information.'''

"""
====================================================
VisionWork AI
Track State
====================================================
"""

from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass(slots=True)
class TrackState:

    track_id: int

    bbox: Tuple[int, int, int, int]

    age: int = 0

    visible: bool = True

    lost_frames: int = 0

    history: List[Tuple[int, int]] = field(default_factory=list)

    @property
    def center(self):

        x1, y1, x2, y2 = self.bbox

        return (
            (x1 + x2) // 2,
            (y1 + y2) // 2,
        )

    def update(self, bbox):

        self.bbox = bbox

        self.history.append(self.center)

        self.age += 1

        self.visible = True

        self.lost_frames = 0

    def mark_lost(self):

        self.visible = False

        self.lost_frames += 1