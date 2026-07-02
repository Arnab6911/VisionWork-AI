"""
====================================================
VisionWork AI
Detection Model
====================================================
"""

from dataclasses import dataclass
from typing import Tuple


@dataclass
class Detection:
    """
    Represents one detected object.
    """

    class_id: int
    class_name: str
    confidence: float
    bbox: Tuple[int, int, int, int]

    def width(self) -> int:
        return self.bbox[2] - self.bbox[0]

    def height(self) -> int:
        return self.bbox[3] - self.bbox[1]

    def center(self):
        return (
            (self.bbox[0] + self.bbox[2]) // 2,
            (self.bbox[1] + self.bbox[3]) // 2,
        )

    def area(self) -> int:
        return self.width() * self.height()

    def to_dict(self):
        return {
            "class_id": self.class_id,
            "class_name": self.class_name,
            "confidence": round(self.confidence, 3),
            "bbox": self.bbox,
        }

    def __str__(self):
        return (
            f"{self.class_name} | "
            f"{self.confidence:.2f} | "
            f"{self.bbox}"
        )