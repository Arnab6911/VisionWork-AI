"""
====================================================
VisionWork AI
Tracking Engine
====================================================
"""

from src.interfaces.tracker import ITracker

from src.adapters.tracking_adapter import TrackingAdapter

from src.tracking.backend import TrackerBackend


class TrackingEngine(ITracker):

    def __init__(self):

        self.backend = TrackerBackend()

    def update(self, detections):

        # Convert our Detection objects
        sv_detections = TrackingAdapter.to_supervision(
            detections
        )

        # ByteTrack
        tracks = self.backend.update(
            sv_detections
        )

        return tracks