import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

def get_finger_count(image):
    
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            lm = hand_landmarks.landmark

            
            finger_tips = [4, 8, 12, 16, 20]
            finger_pips = [2, 6, 10, 14, 18] 

            fingers = []

            
            if lm[17].x < lm[5].x:
               
                fingers.append(lm[4].x > lm[3].x)
            else:
                
                fingers.append(lm[4].x < lm[3].x)

            
            for tip, pip in zip(finger_tips[1:], finger_pips[1:]):
                fingers.append(lm[tip].y < lm[pip].y)

            total_fingers = sum(fingers)

            
            if fingers[0] and all(not f for f in fingers[1:]):
                return -1  

            return total_fingers  

    return None
