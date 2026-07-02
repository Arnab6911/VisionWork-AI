"""
====================================================
VisionWork AI
ByteTrack Backend
====================================================
"""

import supervision as sv


class TrackerBackend:
    """
    Wrapper around ByteTrack.
    This is the ONLY file that knows ByteTrack exists.
    """

    def __init__(self):

        self.tracker = sv.ByteTrack(
            track_activation_threshold=0.25,
            minimum_matching_threshold=0.8,
            lost_track_buffer=30,
            frame_rate=30
        )

    def update(self, detections):

        return self.tracker.update_with_detections(detections)