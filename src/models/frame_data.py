"""
====================================================
VisionWork AI
Frame Data
====================================================
"""

from dataclasses import dataclass, field
from typing import List

from .detection import Detection


@dataclass(slots=True)
class FrameData:

    frame_number: int

    detections: List[Detection] = field(default_factory=list)

    fps: float = 0

    timestamp: float = 0