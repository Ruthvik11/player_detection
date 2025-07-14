import os
import cv2
from ultralytics import YOLO

model= YOLO("models/best.pt")

results = model.track(
    source="input/15sec_input_720p.mp4",  
    tracker="botsort.yaml",             
    save=True,
    persist=True,
    conf=0.3                              
)

print(" Tracking complete. Output saved in 'runs/track/exp/'")
cap = cv2.VideoCapture("runs/track/exp/15sec_input_720p.avi")
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Tracking Output", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()