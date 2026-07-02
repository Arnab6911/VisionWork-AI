"""
Frame Container
"""

from dataclasses import dataclass, field
from typing import List

from src.models.detection import Detection


@dataclass
class FrameData:

    frame_id: int

    detections: List[Detection] = field(default_factory=list)