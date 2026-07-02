import cv2

from camera import Camera
from config import *
from detection.detector import PersonDetector


def main():

    camera = Camera(CAMERA_INDEX)

    detector = PersonDetector(MODEL_NAME)

    while True:

        ret, frame = camera.read()

        if not ret:
            break

        results = detector.detect(frame)

        annotated_frame = results[0].plot()

        cv2.imshow(WINDOW_NAME, annotated_frame)

        key = cv2.waitKey(1)

        if key == ord("q"):
            break

    camera.release()

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()