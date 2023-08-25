#text on image

import cv2
img  = cv2.imread('OIP.jpeg', 1)
font= cv2.FONT_HERSHEY_DUPLEX
nimg = cv2.putText(img , 'subscribe' ,(50 ,50) ,font ,1 ,(0,0,255) ,3) #1 for size of font
cv2.imshow('image' ,nimg )
cv2.waitKey(0)
cv2.destroyAllWindows()
