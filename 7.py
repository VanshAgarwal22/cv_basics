import matplotlib.pyplot as plt
import cv2
img  = cv2.imread('OIP.jpeg', 1)
img= cv2.cvtColor(img ,cv2.COLOR_BGR2RGB)

fr = cv2.imread('th (1).jpeg', 1)
fr= cv2.cvtColor(fr ,cv2.COLOR_BGR2RGB)

butt = cv2.imread('th.jpeg', 1)
butt = cv2.cvtColor(butt ,cv2.COLOR_BGR2RGB)

home = cv2.imread('th (2).jpeg', 1)
home = cv2.cvtColor(home ,cv2.COLOR_BGR2RGB)

images = [img, fr ,butt , home]

for i in range(len(images)):
    plt.subplot(3,2,i+1)
    plt.xticks([]) #for removing numbers in x-axis
    plt.yticks([])
    plt.imshow(images[i])
    


plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()