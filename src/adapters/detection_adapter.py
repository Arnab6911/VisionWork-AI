from src.models import Detection


class DetectionAdapter:

    @staticmethod
    def from_yolo(results, class_names, office_classes):

        detections = []

        for result in results:

            for box in result.boxes:

                cls = int(box.cls[0])

                name = class_names[cls]

                if name not in office_classes:
                    continue

                conf = float(box.conf[0])

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                detections.append(

                    Detection(

                        class_id=cls,

                        class_name=name,

                        confidence=conf,

                        bbox=(x1, y1, x2, y2)

                    )

                )

        return detections