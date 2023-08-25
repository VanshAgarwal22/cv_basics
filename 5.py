#mouse event (print the coordinates on the image where you point your mouse)
import cv2
img  = cv2.imread('OIP.jpeg', 1)
def click_mouse_events(event ,a ,b , flags , params ):
    font= cv2.FONT_HERSHEY_DUPLEX
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.putText(img ,str(a)+',' + str(b), (a,b),font,3,  (0,0,255) , 5) #size color thickness
        cv2.imshow('image' ,img )#update window
        
        
cv2.imshow('image' ,img )
cv2.setMouseCallback('image' ,click_mouse_events)
cv2.waitKey(0)
cv2.destroyAllWindows()
