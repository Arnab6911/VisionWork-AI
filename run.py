import cv2
import time

from src.camera import Camera
from src.config import CAMERA_INDEX, WINDOW_NAME
from src.detection.detector import PersonDetector
from src.ui.draw import Renderer


def main():

    camera = Camera(CAMERA_INDEX)

    detector = PersonDetector()

    renderer = Renderer()

    previous_time = time.time()

    while True:

        ret, frame = camera.read()

        if not ret:
            break

        detections = detector.detect(frame)

        frame = renderer.draw(frame, detections)

        current_time = time.time()

        fps = 1 / (current_time - previous_time)

        previous_time = current_time

        cv2.putText(
            frame,
            f"FPS : {int(fps)}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 255),
            2
        )

        cv2.imshow(WINDOW_NAME, frame)

        key = cv2.waitKey(1)

        if key == ord("q"):
            break

    camera.release()

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()