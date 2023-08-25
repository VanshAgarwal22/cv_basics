#capture frame and switch on your camera

import cv2

cap = cv2.VideoCapture(0) #capture video

while True:
    _,frame = cap.read()
    gray =cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    cv2.imshow('Frame window' ,gray)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

    
    
    
