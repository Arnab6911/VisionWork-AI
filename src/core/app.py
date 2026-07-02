"""
====================================================
VisionWork AI
Application Controller
====================================================
"""

import cv2

from src.core.pipeline import VisionPipeline
from src.config import WINDOW_NAME


class VisionApp:

    def __init__(self):
        self.pipeline = VisionPipeline()

    def run(self):

        while True:

            frame = self.pipeline.process()

            if frame is None:
                break

            cv2.imshow(WINDOW_NAME, frame)

            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break

        self.pipeline.release()

        cv2.destroyAllWindows()