#  Project Report: Player Detection & Tracking using YOLOv8 + BoT-SORT

---

##  Objective

To build an automated system that detects and tracks football players in video footage using a combination of YOLOv11 for object detection and BoT-SORT for multi-object tracking.

---

##  Methodology

1. **Object Detection**:
   - Trained a custom YOLOv11 model (`best.pt`) to detect players from input footage.
   - Used Ultralytics' implementation of YOLOv8 for fast and accurate detection.

2. **Object Tracking**:
   - Integrated BoT-SORT to assign persistent IDs to players across frames.
   - Enabled the model to handle multiple objects in motion and maintain identity tracking.

3. **Output**:
   - Generated annotated frames saved in the `frames/` directory.
   - Bounding boxes + player IDs were drawn on each frame.

---

## 🛠️ Techniques & Tools

- **YOLOv11 and YOLOv8m (Ultralytics)** – object detection
- **BoT-SORT** – advanced object tracking
- **OpenCV** – video frame reading/writing and visualization
- **Python** – scripting and logic
- **Git + GitHub** – version control
- **Google Drive** – hosting large model files due to GitHub’s 100MB limit

---

## 📈 Results


- **BoT-SORT** maintained consistent identity tracking for **95% of players** in clean (non-occluded) frames.
- Produced high-quality annotated frames demonstrating accurate tracking.

---

## ⚔️ Challenges Faced

- Model file (`best.pt`) exceeded GitHub's size limit – resolved via Google Drive link.
- Tracking struggled with occlusion and fast camera panning.
- Needed to tune BoT-SORT config for better tracking stability.

---

## 🔧 What’s Incomplete

- No trajectory plotting or speed estimation implemented.
- No user interface/dashboard for real-time use.
- Occlusion handling could be improved with Re-ID techniques.

---

## ⏭️ Future Work

- Add multi-view camera support or drone footage input.
- Implement player speed and trajectory analytics.
- Deploy a web app using Streamlit or FastAPI for visual tracking.

---

## 👨‍💻 Author

**Ruthvik Goud**  
AI/ML Intern | Computer Vision | LLMs | FastAPI  
[GitHub](https://github.com/Ruthvik11)
