"""
====================================================
VisionWork AI
YOLO Detection Engine
====================================================
"""

from ultralytics import YOLO

from src.config import (
    MODEL_NAME,
    DEVICE,
    CONFIDENCE_THRESHOLD,
    OFFICE_CLASSES,
)

from src.models.detection import Detection


class PersonDetector:

    def __init__(self):

        print("=" * 50)
        print("Loading VisionWork Detection Engine...")
        print("=" * 50)

        self.model = YOLO(MODEL_NAME)

        self.class_names = self.model.names

        print(f"Model Loaded : {MODEL_NAME}")
        print(f"Device       : {DEVICE}")
        print("=" * 50)

    def detect(self, frame):

        results = self.model(
            frame,
            conf=CONFIDENCE_THRESHOLD,
            device=DEVICE,
            verbose=False
        )

        detections = []

        for result in results:

            for box in result.boxes:

                class_id = int(box.cls[0])

                class_name = self.class_names[class_id]

                if class_name not in OFFICE_CLASSES:
                    continue

                confidence = float(box.conf[0])

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                detections.append(

                    Detection(

                        class_id=class_id,

                        class_name=class_name,

                        confidence=confidence,

                        bbox=(x1, y1, x2, y2)

                    )

                )

        return detections