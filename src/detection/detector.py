from ultralytics import YOLO
class PersonDetector:
    def __init__(self,model):
        self.model=YOLO(model)
    def detect(self,frame):
        return self.model(frame,verbose=False)
