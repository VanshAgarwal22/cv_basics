#filters in open  -->> gaussian blurring --.for removing gaussain noise

import cv2
import matplotlib.pyplot as plt
img  = cv2.imread('OIP.jpeg', 1)
img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
blur = cv2.blur(img ,(5,5))

#gaussian blurrimg
gaussian = cv2.GaussianBlur(img , (5,5) ,0)


titles = ['original' ,'Average' , 'Gaussian']
images = [img , blur ,gaussian]

for i in range(len(images)):
    plt.subplot(2
                ,2,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
plt.show()



