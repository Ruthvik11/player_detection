#  Project Report: Football Player Tracking using YOLOv8 + BoT-SORT

## Introduction
This project implements a real-time football player tracking system using YOLOv8 for object detection and BoT-SORT for multi-object tracking. The goal is to detect and track players in football match videos, assigning consistent IDs to each player across frames for applications in sports analytics.
---

##  Methodology

This project uses a YOLOv8 object detection model trained on football players to detect players in each frame. For multi-object tracking, we integrated BoT-SORT (Better SORT) to assign consistent IDs to each player across frames.

The pipeline also extracts each frame with bounding boxes and ID overlays.

---

## ⚙ Techniques Used

- **YOLOv11 (Ultralytics)** for real-time object detection
- **YOLOv8m and YOLOv8n  (Ultralytics)** also tried this for object detection
- **BoT-SORT** for object tracking with identity consistency
- **OpenCV** for frame-by-frame extraction and saving outputs
- **Google Drive** hosting for large model weight files

---


---
##  Challenges Faced

- Tracking failed for occluded or overlapping players in early attempts
- GitHub's 100MB limit blocked the model file upload
- Required model tuning and video resolution adjustments for better detection

---

##  What’s Incomplete

- No trajectory plotting or speed estimation
- No web interface (e.g., Streamlit or FastAPI dashboard)

---

##  Future Improvements

- Train on larger datasets with labeled teams
- Use higher-quality videos with multiple camera angles
- Deploy a real-time dashboard for match analytics

---

##  Built By

Ruthvik Goud
ML & Computer Vision Enthusiast
Gmail : ruthviksayabugari@gmail.com
Github : https://github.com/Ruthvik11
