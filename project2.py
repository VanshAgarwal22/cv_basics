#  eye and face detection
import cv2
face_classifier = cv2.CascadeClassifier("C:/Users/Vansh/anaconda3/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
eye_classifier = cv2.CascadeClassifier("C:/Users/Vansh/anaconda3/Lib/site-packages/cv2/data/haarcascade_eye.xml")
cap = cv2.VideoCapture(0)
while(cap.isOpened()): #continue the while loop
    _,frame = cap.read() #contain two parameter  frame for image
    gray = cv2.cvtColor(frame ,cv2.COLOR_BGR2GRAY) #convewrt into  gray scale
    faces = face_classifier.detectMultiScale(gray) #detect
    
    for x,y,w,h in faces:
        cv2.rectangle(frame , (x,y) ,(x+w , y+h), (0,0,255) ,3) # 3 is width of the rectangle line
        roi_color = frame[y:y+h , x:x+w] # region of interest
        roi_gray = frame[y:y+h ,x:x+w]
        eye = eye_classifier.detectMultiScale(roi_gray)
        for ex,ey,ew,eh in eye:
            cv2.rectangle(roi_color , (ex,ey) ,(ex+ew , ey+eh), (255,0,0) ,3)
    cv2.imshow('Video' , frame)
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()