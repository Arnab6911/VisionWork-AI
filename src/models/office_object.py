"""
====================================================
VisionWork AI
Office Object
====================================================
"""

from dataclasses import dataclass
from typing import Tuple


@dataclass(slots=True)
class OfficeObject:

    class_name: str

    confidence: float

    bbox: Tuple[int, int, int, int]

    @property
    def center(self):

        x1, y1, x2, y2 = self.bbox

        return (

            (x1 + x2) // 2,

            (y1 + y2) // 2,

        )