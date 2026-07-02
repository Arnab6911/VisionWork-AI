import cv2,time
from src.camera import Camera
from src.config import *
from src.detection.detector import PersonDetector
from src.ui.draw import draw_detections

cam=Camera(CAMERA_INDEX)
detector=PersonDetector(MODEL_NAME)

prev=time.time()

while True:
    ok,frame=cam.read()
    if not ok:
        break
    results=detector.detect(frame)
    fps=1/(time.time()-prev)
    prev=time.time()
    frame=draw_detections(frame,results,fps)
    cv2.imshow(WINDOW_NAME,frame)
    if cv2.waitKey(1)&0xFF==ord("q"):
        break
cam.release()
cv2.destroyAllWindows()
