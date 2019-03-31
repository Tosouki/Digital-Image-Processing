import numpy as np
import cv2
from matplotlib import pyplot as plt
#載入圖片
img = cv2.imread('pout.tif')
gray = cv2.imread('pout.tif')
#得知圖片大小
sp=img.shape

fig = np.arange(0,256)
num = np.zeros(256)
num2 = np.zeros(256)
num3 = np.zeros(256)
minn = 0
val2 = 0
#直方圖
for x in range(0,sp[0]):
    for y in range(0,sp[1]):
        val=img[x,y]
        num[val]+=1        
#找到最小值並累積分布函數
for y in range(0,256):
    if num[y]>0 and minn==0:
        minn=num[y]        
    if num[y]>0:       
        num2[y]=num[y]+num2[val2]
        val2=y   
#改變圖片像素並製作等化直方圖        
for x in range(0,sp[0]):
    for y in range(0,sp[1]):
        gray[x,y]=np.round((num2[gray[x,y]]-minn)/(291*240-minn)*255)
        val=gray[x,y]
        num3[val]+=1
#顯示結果 
plt.subplot(2,2,1)          
plt.axis('off')
plt.imshow(img)
plt.subplot(2,2,2)          
plt.axis('off')
plt.imshow(gray)        
plt.subplot(2,2,3)        
plt.plot(fig,num[fig])        
plt.subplot(2,2,4)          
plt.plot(fig,num3[fig]) 
plt.show()
