import cv2
class Camera:
    def __init__(self,index=0):
        self.cap=cv2.VideoCapture(index)
        if not self.cap.isOpened():
            raise RuntimeError("Camera not found")
    def read(self):
        return self.cap.read()
    def release(self):
        self.cap.release()
