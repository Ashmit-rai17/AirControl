import cv2 as cv
import mediapipe as mp
import numpy as np
import pyautogui
from collections import deque

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

cap = cv.VideoCapture(0)


def play_pause():
    pyautogui.press("space")

def next_track():
    pyautogui.hotkey("ctrl", "right")

def volume_up():
    pyautogui.press("volumeup")

def volume_down():
    pyautogui.press("volumedown")


gesture_history = deque(maxlen=5)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv.flip(frame, 1)  # Mirror effect
    frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    detected_gesture = None  # Store current detected gesture

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            h, w, _ = frame.shape
            landmarks = []

            # Store landmark positions
            for lm in hand_landmarks.landmark:
                cx, cy = int(lm.x * w), int(lm.y * h)
                landmarks.append((cx, cy))

            landmarks_np = np.array(landmarks, dtype=np.int32)
            hull_indices = cv.convexHull(landmarks_np, returnPoints=False)
            hull_indices = np.array(sorted(hull_indices.flatten()), dtype=np.int32).reshape(-1, 1)

            if len(hull_indices) > 4: 
                defects = cv.convexityDefects(landmarks_np, hull_indices)
                if defects is not None:
                    count_fingers = 0
                    for i in range(defects.shape[0]):
                        s, e, f, d = defects[i, 0]
                        start = tuple(landmarks_np[s])
                        end = tuple(landmarks_np[e])
                        far = tuple(landmarks_np[f])

                        a = np.linalg.norm(np.array(start) - np.array(end))
                        b = np.linalg.norm(np.array(start) - np.array(far))
                        c = np.linalg.norm(np.array(end) - np.array(far))

                        angle = np.degrees(np.arccos((b**2 + c**2 - a**2) / (2 * b * c)))

                        if angle < 90:
                            count_fingers += 1
                            cv.circle(frame, far, 5, (0, 0, 255), -1)

                
                if count_fingers == 5:
                    detected_gesture = "Play/Pause"
                elif count_fingers == 1:
                    detected_gesture = "Volume Up"
                elif count_fingers == 4:
                    detected_gesture = "Next Track"
                elif count_fingers == 3:
                    detected_gesture = "Volume Down"

   
    if detected_gesture:
        gesture_history.append(detected_gesture)
        most_common_gesture = max(set(gesture_history), key=gesture_history.count)

    
        if gesture_history.count(most_common_gesture) >= 3:
            if most_common_gesture == "Play/Pause":
                play_pause()
            elif most_common_gesture == "Volume Up":
                volume_up()
            elif most_common_gesture == "Next Track":
                next_track()
            elif most_common_gesture == "Volume Down":
                volume_down()

            cv.putText(frame, most_common_gesture, (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv.imshow("Gesture Media Control", frame)

    if cv.waitKey(1) & 0xFF == ord('d'):
        break

cap.release()
cv.destroyAllWindows()
