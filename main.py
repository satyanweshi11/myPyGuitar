import cv2
from hand_tracking import get_finger_count
from chord_manager import update_chord

cap = cv2.VideoCapture(0)
previous_chord = None 

while True:
    success, img = cap.read()
    if not success:
        break

    
    finger_count = get_finger_count(img)

    if finger_count is not None:  
        current_chord = update_chord(finger_count)

        if current_chord and current_chord != previous_chord:  
            previous_chord = current_chord  

    else:
        previous_chord = None 

    
    cv2.putText(img, f"Chord: {current_chord if finger_count is not None else 'No Hand'}",
                (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow("Air Guitar - Chord Selector", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
