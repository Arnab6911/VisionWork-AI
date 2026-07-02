"""
VisionWork Pipeline
"""

from src.camera import Camera
from src.detection.detector import PersonDetector
from src.ui.draw import Renderer


class VisionPipeline:

    def __init__(self):

        self.camera = Camera()

        self.detector = PersonDetector()

        self.renderer = Renderer()

    def process(self):

        ret, frame = self.camera.read()

        if not ret:

            return None

        detections = self.detector.detect(frame)

        frame = self.renderer.draw(frame, detections)

        return frame

    def release(self):

        self.camera.release()