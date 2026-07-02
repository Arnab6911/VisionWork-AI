"""
====================================================
VisionWork AI
Central Frame Container
====================================================
"""

from dataclasses import dataclass, field
from typing import List

from .detection import Detection
from .employee import Employee
from .office_object import OfficeObject


@dataclass(slots=True)
class FrameData:
    """
    Central object passed through the entire pipeline.
    Every module updates this object.
    """

    # Original Camera Frame
    frame: any

    # Frame Information
    frame_number: int = 0
    fps: float = 0.0
    timestamp: float = 0.0

    # Detection Results
    detections: List[Detection] = field(default_factory=list)

    # Tracking / Workforce
    workforce: List[Employee] = field(default_factory=list)

    # Office Objects
    office_objects: List[OfficeObject] = field(default_factory=list)

    # Future Modules
    alerts: List[str] = field(default_factory=list)

    events: List[str] = field(default_factory=list)

    camera_name: str = "Camera-1"

    status: str = "Running"