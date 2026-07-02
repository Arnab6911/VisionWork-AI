"""
====================================================
VisionWork AI
Detection Engine
====================================================
"""

from ultralytics import YOLO

from src.config import (
    MODEL_PATH,
    DEVICE,
    CONFIDENCE_THRESHOLD,
    OFFICE_CLASSES,
)

from src.models import Detection


class DetectionEngine:

    def __init__(self):

        print("=" * 60)
        print("Loading Detection Engine...")
        print("=" * 60)

        self.model = YOLO(str(MODEL_PATH))

        self.class_names = self.model.names

        print(f"Model : {MODEL_PATH.name}")
        print(f"Device: {DEVICE}")

        print("=" * 60)

    def detect(self, frame):

        results = self.model(
            frame,
            conf=CONFIDENCE_THRESHOLD,
            device=DEVICE,
            verbose=False,
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
                        bbox=(x1, y1, x2, y2),
                    )

                )

        return detections