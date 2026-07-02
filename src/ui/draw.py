"""
====================================================
VisionWork AI
Professional Renderer
====================================================
"""

import cv2

from src.config import (
    COLORS,
    BOX_THICKNESS,
    FONT_SCALE,
    FONT_THICKNESS,
    SHOW_CONFIDENCE,
)


class Renderer:

    def __init__(self):
        pass

    def draw(self, frame, detections):

        for detection in detections:

            x1, y1, x2, y2 = detection.bbox

            class_name = detection.class_name

            confidence = detection.confidence

            color = COLORS.get(
                class_name,
                COLORS["default"]
            )

            # Bounding Box
            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                color,
                BOX_THICKNESS
            )

            # Label
            if SHOW_CONFIDENCE:
                label = f"{class_name} {confidence:.2f}"
            else:
                label = class_name

            (w, h), _ = cv2.getTextSize(
                label,
                cv2.FONT_HERSHEY_SIMPLEX,
                FONT_SCALE,
                FONT_THICKNESS
            )

            cv2.rectangle(
                frame,
                (x1, y1 - 30),
                (x1 + w + 10, y1),
                color,
                -1
            )

            cv2.putText(
                frame,
                label,
                (x1 + 5, y1 - 8),
                cv2.FONT_HERSHEY_SIMPLEX,
                FONT_SCALE,
                (255, 255, 255),
                FONT_THICKNESS
            )

        return frame