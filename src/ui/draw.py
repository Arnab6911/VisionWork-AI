"""
====================================================
VisionWork AI
Professional Renderer
====================================================
"""

import cv2

from src.interfaces.renderer import IRenderer
from src.config import (
    COLORS,
    BOX_THICKNESS,
    FONT_SCALE,
    FONT_THICKNESS,
)


class Renderer(IRenderer):

    def __init__(self):
        pass

    def draw(self, frame_data):

        frame = frame_data.frame

        workforce = frame_data.workforce

        # Draw Employees
        for employee in workforce:

            x1, y1, x2, y2 = employee.bbox

            color = COLORS.get("person", (0, 255, 0))

            # Bounding Box
            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                color,
                BOX_THICKNESS
            )

            # Background Label
            cv2.rectangle(
                frame,
                (x1, y1 - 55),
                (x1 + 220, y1),
                color,
                -1
            )

            # Employee ID
            cv2.putText(
                frame,
                f"Employee #{employee.track_id}",
                (x1 + 5, y1 - 35),
                cv2.FONT_HERSHEY_SIMPLEX,
                FONT_SCALE,
                (255, 255, 255),
                FONT_THICKNESS
            )

            # Status
            cv2.putText(
                frame,
                employee.status,
                (x1 + 5, y1 - 15),
                cv2.FONT_HERSHEY_SIMPLEX,
                FONT_SCALE,
                (255, 255, 255),
                FONT_THICKNESS
            )

        # -----------------------------
        # FPS
        # -----------------------------

        cv2.putText(
            frame,
            f"FPS : {int(frame_data.fps)}",
            (20, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 255),
            2
        )

        # -----------------------------
        # Employee Count
        # -----------------------------

        cv2.putText(
            frame,
            f"Employees : {len(workforce)}",
            (20, 70),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        frame_data.frame = frame

        return frame_data