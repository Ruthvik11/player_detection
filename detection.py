import cv2
import os
from ultralytics import YOLO

model = YOLO("D:\player_detection\models\best.pt")

video = cv2.VideoCapture("input/15sec_input_720p.mp4")

width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(video.get(cv2.CAP_PROP_FPS))

fourcc= cv2.VideoWriter_fourcc(*"mp4v")
out_video = cv2.VideoWriter("output/detected3.mp4", fourcc,fps,( width,height))

while video.isOpened():
    frame_exists, frame = video.read()
    if not frame_exists:
        break

    results = model(frame)


    for result in results:
        for box in result.boxes:
            x1,y1,x2,y2 = map(int,box.xyxy[0])
            conf = float(box.conf)
            class_box = int(box.cls)

     
        if conf > 0.3:
            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.putText(frame, f"Player {class_box}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    out_video.write(frame)
    #cv2.imshow("YOLOv11 Detection", frame)
    #if cv2.waitKey(1) == ord('q'):
        #break

video.release()
out_video.release()
cv2.destroyAllWindows()

model = YOLO("best.pt")
results = model.track(
    source="input/15sec_input_720p.mp4",
    tracker="botsort.yaml",  # enable BoT-SORT
    persist=True,
    save=True
)

