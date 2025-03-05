# AirControl
📌 Task 1: Project Setup & Basic Image Processing
Objective: Set up the development environment and preprocess video feed.
🔹 Subtasks:
1. Install required libraries: OpenCV, Mediapipe, pyautogui, and pycaw.
2. Capture live video feed using OpenCV. (Docs)
3. Convert frames to grayscale and apply thresholding. (Docs)
4. Perform edge detection using Canny. (Docs)
✅ GitHub Action:
● Create a GitHub repository named AirControl.
● Initialize the repository with a README file.
● Add a .gitignore file (Python-specific).
● First commit: Upload the basic project structure.
📌 Task 2: Hand Detection & Landmark Extraction
Objective: Detect hands in real-time and extract key points.
🔹 Subtasks:
1. Use Mediapipe’s Hand Tracking module to detect hands. (Docs)
2. Extract and visualize key hand landmarks.
3. Map the coordinates of important fingers (index, thumb, etc.).
4. Draw hand skeletons using OpenCV’s drawing utilities. (Docs)
✅ GitHub Action:
● Commit and push code updates for hand tracking.
● Update README with progress details.
📌 Task 3: Gesture Recognition
Objective: Identify and classify hand gestures.
🔹 Subtasks:
1. Use Convex Hull to detect open fingers. (Docs)
2. Define gestures for media control:
○ ✋ Open Palm → Play/Pause
○ ☝️ One Finger → Volume Up
○ ✌️ Two Fingers → Next Track
○ ✊ Fist → Volume Down
3. Filter out noise to prevent false positives.
✅ GitHub Action:
● Create a gestures.py file and push changes.
● Update documentation explaining gesture detection logic.
📌 Task 4: Gesture-Based Media Control
Objective: Use gestures to control system media functions.
🔹 Subtasks:
1. Integrate pycaw for volume control.
2. Use pyautogui or keyboard for media playback control.
3. Map gesture detection output to media actions.
📌 Resources:
● pycaw – Windows Audio Control
● pyautogui – Automate GUI interactions
✅ GitHub Action:
● Commit and push media control integration.
● Update README with instructions on usage.
📌 Task 5: Performance Optimization & UI
Objective: Improve performance and add a simple interface.
🔹 Subtasks:
1. Reduce processing lag by optimizing frame rate.
2. Improve gesture recognition accuracy with filtering techniques.
3. Create a Tkinter/PyQt UI to display detected gestures in real time.
📌 Resources:
● Optimizing OpenCV for Real-Time Performance
● Tkinter GUI Basics
✅ GitHub Action:
● Push UI implementation updates.
● Add screenshots of the working UI in the README.
📌 Task 6: Testing, Debugging & Final Deployment
Objective: Test, fix bugs, and document the project.
🔹 Subtasks:
1. Test gestures in different lighting conditions.
2. Fix misdetections and refine thresholds.
3. Create a README with project details and installation steps.
4. Record a demo video showing how the system works.
📌 Final Deliverables:
✅ Working Aur Control system. ✅ Complete documentation & codebase. ✅ Demo video showcasing all functionalities.
✅ GitHub Action:
● Upload the final cleaned-up code.
● Add an installation guide to the README.
● Push the demo video and screenshots to the repo.
🛠 GitHub Workflow Summary
1. Create and initialize a repository (git init, git add ., git commit -m
"Initial commit", git push origin main).
