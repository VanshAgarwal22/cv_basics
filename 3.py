#dray something on image

import cv2
img  = cv2.imread('OIP.jpeg', 1)
# cv2.line(img ,(0,0),(500,255) , (567,255,0) ,2)
# cv2.rectangle(img , (0,0) ,(200, 200) ,(0,0,255), 4)
cv2.circle(img, (255,255) ,40 , (255,0,0) ,5)
cv2.imshow('image' ,img)
cv2.waitKey(0)
cv2.destroyAllWindows()

