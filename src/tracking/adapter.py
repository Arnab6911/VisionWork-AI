'''adapter.py

Converts

Detection

↓

supervision.Detections

and back again.

This allows us to replace ByteTrack later without changing the project.'''


"""
====================================================
VisionWork AI
Tracking Adapter
====================================================
"""

import numpy as np
import supervision as sv

from src.models import Detection


class TrackingAdapter:

    def to_supervision(self, detections):

        if len(detections) == 0:

            return sv.Detections.empty()

        xyxy = []

        confidence = []

        class_id = []

        for det in detections:

            xyxy.append(det.bbox)

            confidence.append(det.confidence)

            class_id.append(det.class_id)

        return sv.Detections(

            xyxy=np.array(xyxy),

            confidence=np.array(confidence),

            class_id=np.array(class_id),

        )