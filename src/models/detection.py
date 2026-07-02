"""
====================================================
VisionWork AI
Detection Model
====================================================
"""

from dataclasses import dataclass
from typing import Tuple


@dataclass(slots=True)
class Detection:

    class_id: int
    class_name: str
    confidence: float
    bbox: Tuple[int, int, int, int]

    @property
    def x1(self):
        return self.bbox[0]

    @property
    def y1(self):
        return self.bbox[1]

    @property
    def x2(self):
        return self.bbox[2]

    @property
    def y2(self):
        return self.bbox[3]

    @property
    def width(self):
        return self.x2 - self.x1

    @property
    def height(self):
        return self.y2 - self.y1

    @property
    def center(self):

        return (

            (self.x1 + self.x2) // 2,

            (self.y1 + self.y2) // 2,

        )

    @property
    def area(self):

        return self.width * self.height

    def to_dict(self):

        return {

            "class_id": self.class_id,

            "class_name": self.class_name,

            "confidence": self.confidence,

            "bbox": self.bbox,

        }