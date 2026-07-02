"""
====================================================
VisionWork AI
Main Processing Pipeline
====================================================
"""

import time

from src.camera import Camera
from src.config import CAMERA_INDEX

from src.models import FrameData

from src.detection import DetectionEngine
from src.tracking import TrackingEngine
from src.managers import WorkforceManager
from src.ui.draw import Renderer


class VisionPipeline:

    def __init__(self):

        print("=" * 60)
        print("Initializing VisionWork AI...")
        print("=" * 60)

        self.camera = Camera(CAMERA_INDEX)

        self.detector = DetectionEngine()

        self.tracker = TrackingEngine()

        self.workforce_manager = WorkforceManager()

        self.renderer = Renderer()

        self.frame_number = 0

        self.previous_time = time.time()

    def process(self):

        ret, frame = self.camera.read()

        if not ret:
            return None

        self.frame_number += 1

        current_time = time.time()

        fps = 1 / max(current_time - self.previous_time, 1e-6)

        self.previous_time = current_time

        # -----------------------------------------
        # Create FrameData
        # -----------------------------------------

        frame_data = FrameData(

            frame=frame,

            frame_number=self.frame_number,

            fps=fps,

            timestamp=current_time

        )

        # -----------------------------------------
        # Detection
        # -----------------------------------------

        frame_data.detections = self.detector.detect(

            frame_data.frame

        )

        # -----------------------------------------
        # Tracking
        # -----------------------------------------

        tracks = self.tracker.update(

            frame_data.detections

        )

        # -----------------------------------------
        # Workforce
        # -----------------------------------------

        frame_data.workforce = list(

            self.workforce_manager.update(tracks).values()

        )

        # -----------------------------------------
        # Renderer
        # -----------------------------------------

        frame_data = self.renderer.draw(frame_data)

        return frame_data.frame

    def release(self):

        self.camera.release()