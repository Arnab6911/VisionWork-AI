import numpy as np
import supervision as sv


class TrackingAdapter:

    @staticmethod
    def to_supervision(detections):

        if len(detections) == 0:

            return sv.Detections.empty()

        xyxy = np.array([d.bbox for d in detections])

        confidence = np.array([d.confidence for d in detections])

        class_id = np.array([d.class_id for d in detections])

        return sv.Detections(

            xyxy=xyxy,

            confidence=confidence,

            class_id=class_id

        )