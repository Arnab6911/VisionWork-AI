import cv2

def draw_detections(frame,results,fps):
    r=results[0]
    for b in r.boxes:
        cls=int(b.cls[0])
        if cls!=0:
            continue
        x1,y1,x2,y2=map(int,b.xyxy[0])
        conf=float(b.conf[0])
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
        cv2.rectangle(frame,(x1,y1-28),(x2,y1),(0,255,0),-1)
        cv2.putText(frame,f"Employee {conf:.2f}",(x1+5,y1-8),
                    cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,0),2)
    cv2.putText(frame,f"FPS: {fps:.1f}",(20,35),
                cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2)
    return frame
