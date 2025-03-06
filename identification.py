import cv2 as cv
import mediapipe as mp
import numpy as np
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
cap = cv.VideoCapture(0)

while True:
    ret , frame = cap.read()
    frame = cv.flip(frame , 1)

    frame_rgb = cv.cvtColor(frame , cv.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
             h, w, _ = frame.shape
             landmarks = []

             for lm in hand_landmarks.landmark:
                 cx , cy = int(lm.x*w) , int(lm.y*h)
                 landmarks.append((cx , cy))
             landmarks_np = np.array(landmarks , dtype=np.int32)
             hull =  cv.convexHull(landmarks_np)
             cv.polylines(frame , [hull] , True , (0 , 255 , 0) , 2)

             hull_indices = cv.convexHull(landmarks_np , returnPoints=False)
             hull_indices = sorted(hull_indices.flatten())  # Ensure monotonic order
             hull_indices = np.array(hull_indices, dtype=np.int32).reshape(-1, 1)
             if len(landmarks_np)>3:
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
                            cv.circle(frame , far , 5 , (0 , 0 , 255) , -1)
                     cv.putText(frame , f"Fingers: {count_fingers+1}" , (50 , 50) , cv.FONT_HERSHEY_SIMPLEX , 1 , (255 , 0 , 0) , 2)
    cv.imshow("Convex hull" , frame)

    if cv.waitKey(1) & 0xff == ord('d'):
        break
cap.release()
cv.destroyAllWindows()