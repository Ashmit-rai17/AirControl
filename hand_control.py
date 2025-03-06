import cv2 as cv
import mediapipe as mp
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.65, min_tracking_confidence=0.65)


cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

while True:
    ret, frame = cap.read()
    frame = cv.flip(frame, 1)

    
    frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

   
    results = hands.process(frame_rgb)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS , mp_draw.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=4),
                                   mp_draw.DrawingSpec(color=(255, 0, 0), thickness=2))
            

            h, w, _ = frame.shape 
            
            key_fingers = {
                "Thumb Tip": (hand_landmarks.landmark[4].x * w, hand_landmarks.landmark[4].y * h),
                "Index Tip": (hand_landmarks.landmark[8].x * w, hand_landmarks.landmark[8].y * h),
                "Middle Tip": (hand_landmarks.landmark[12].x * w, hand_landmarks.landmark[12].y * h),
                "Ring Tip": (hand_landmarks.landmark[16].x * w, hand_landmarks.landmark[16].y * h),
                "Pinky Tip": (hand_landmarks.landmark[20].x * w, hand_landmarks.landmark[20].y * h)
            }
            for name , (x,y) in key_fingers.items():
                cx , cy = int(x) , int(y)
                cv.circle(frame , (cx , cy) , 8 , (0 , 255 , 0) , -1)
                cv.putText(frame , name , (cx-40 , cy-10) , cv.FONT_HERSHEY_SIMPLEX , 0.5 , (255 , 0 , 0))


    cv.imshow('Hand Tracking', frame)

    
    if cv.waitKey(1) & 0xFF == ord('d'):
        break


cap.release()
cv.destroyAllWindows()
