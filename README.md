# Meta Spatial AI Assistant

A Wearable Spatial AI Assistant combining Smart Glasses AR HUD with Smart Ring Micro-Gesture Controls, powered by **Meta Model API (SAM 3.1 & Muse Spark)**.

## 🌟 Overview
This project simulates a completely hands-free, low-friction spatial productivity experience. By using subtle micro-gestures on a smart ring (clicking, selecting, scrolling), users can interact seamlessly with an AR HUD display on smart glasses without needing to raise their arms.

- **SAM 3.1 (Segment Anything Model)**: Performs real-time visual segmentation on objects or live documents selected in the user's field of view.
- **Muse Spark**: Contextual reasoning agent that summarizes documents, executes smart environment actions, and extracts actionable tasks.

## 🛠 Tech Stack
- **Backend**: Python 3.14, FastAPI, Uvicorn, Pydantic
- **Frontend / HUD Simulator**: HTML5, CSS3 (Glassmorphism AR HUD), Modern JavaScript (Fetch API)
- **AI Engine**: Meta Model API (SAM 3.1 & Muse Spark)

## 🚀 Quick Start

1. **Clone Repository**:
   ```bash
   git clone [https://github.com/ekorusd/meta-spatial-assistant.git](https://github.com/ekorusd/meta-spatial-assistant.git)
   cd meta-spatial-assistant

2. Install Dependencies:

Bash
pip install fastapi uvicorn python-multipart --break-system-packages

3. Run Application:

Bash
python3 -m uvicorn main:app --reload

