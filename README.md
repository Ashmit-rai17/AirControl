# AirControl
A tutorial on how to use the following air control module 
# Gesture-Based Media Control

## Overview
This project is a **gesture-based media control system** using **OpenCV**, **MediaPipe**, and **PyAutoGUI**. It allows users to control media playback using **hand gestures** detected via a webcam.

### Features
- **Open Palm (✋)** → Play/Pause (Spacebar)
- **One Finger (☝️)** → Volume Up
- **Two Fingers (✌️)** → Next Track
- **Fist (✊)** → Volume Down
- Uses a **moving average filter** to reduce false positives

---
## Installation

### Prerequisites
Ensure you have Python installed (>= 3.7).

### Install Dependencies
Run the following command to install required packages:

pip install opencv-python mediapipe numpy pyautogui

---
## Usage

### Run the Gesture Control Script
```bash
python gesture_control.py
```

### Controls
| Gesture  | Action        |
|----------|--------------|
| Open Palm (✋) | Play/Pause |
| One Finger (☝️) | Volume Up |
| Two Fingers (✌️) | Next Track |
| Fist (✊) | Volume Down |

To exit, press **'d'**.

---
## How It Works
1. Captures video from webcam.
2. Detects hand landmarks using **MediaPipe**.
3. Computes convex hull and defects to determine the number of extended fingers.
4. Uses a **deque-based smoothing technique** to avoid flickering gestures.
5. Triggers appropriate **PyAutoGUI** keyboard commands for media control.

---
## Troubleshooting
- If gestures are not detected, **increase lighting** and ensure your hand is clearly visible.
- If controls trigger too often, **adjust the smoothing threshold** (`gesture_history.count(most_common_gesture) >= 3`).

---
## Contribution
Feel free to fork the repository and submit **pull requests**!



