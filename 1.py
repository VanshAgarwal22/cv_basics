import cv2


# store image in a variable
img = cv2.imread('OIP.jpeg' ,1) # 1 means same  ,  0 means image in grey scale 
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)#convert original into  gray
cv2.imshow('fgay_sample', gray) # windowname , image
cv2.waitKey(0) # 0 shows when we press red cross ans esc the window cut
cv2.destroyAllWindows()
