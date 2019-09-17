import numpy as np
import cv2
from matplotlib import pyplot as plt

img=cv2.imread('twins_sp.png')
twi=cv2.imread('twins_sp1.png')

sp=img.shape
sp2=twi.shape

num = np.zeros([sp[0],sp[1]])
num2 = np.zeros([sp2[0],sp2[1]])

for x in range(0,sp[0]):
    for y in range(0,sp[1]):
        num[x,y]=img[x,y,1]
for x in range(0,sp2[0]):
    for y in range(0,sp2[1]):
        num2[x,y]=twi[x,y,1]        
for x in range(1,sp[0]-1):
    for y in range(1,sp[1]-1):
        number=(num[(x),(y)]+num[(x),(y+1)]+num[(x),(y-1)]+num[(x+1),(y)]+num[(x+1),(y-1)]+num[(x-1),(y-1)]+num[(x-1),(y)]+num[(x-1),(y+1)])/8
        g=abs(num[(x+1),(y+1)]-number)
        if g>0.2:
            img[x,y]=number
            
for x in range(1,sp2[0]-1):
    for y in range(1,sp2[1]-1):
        number2=(num2[(x),(y)]+num2[(x),(y+1)]+num2[(x),(y-1)]+num2[(x+1),(y)]+num2[(x+1),(y-1)]+num2[(x-1),(y-1)]+num2[(x-1),(y)]+num2[(x-1),(y+1)])/8
        h=abs(num2[(x+1),(y+1)]-number2)
        if h>0.4:
            twi[x,y]=number2   
            
plt.subplot(1,2,1)          
plt.axis('off')
plt.imshow(img)
plt.subplot(1,2,2)          
plt.axis('off')
plt.imshow(twi)
plt.show()
