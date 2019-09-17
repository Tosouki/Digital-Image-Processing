import numpy as np
import cv2
from matplotlib import pyplot as plt

def OTSU(img_array):
    height = img_array.shape[0]
    width = img_array.shape[1]
    count = np.zeros(256)
    pixelPro = np.zeros(256)
#統計每個灰度中像素的個數     
    for x in range(height):
        for y in range(width):
               val=img_array[x,y]
               count[val]+=1       
#計算每個灰度的像素數目占整張圖像的比例
    for x in range(256):
        pixelPro[x] = (float)(count[x]+1/(height*width))
                
    max_var = 0.0
    best_thresold = 0
    for thresold in range(256):#測試0-255找尋最佳閥值        
        w0 = w1 = u0tmp = u1tmp = 0.0
        for i in range(256):
            if i <= thresold:#背景
                w0 += pixelPro[i]
                u0tmp += i * pixelPro[i]
            else:           #前景
                w1 += pixelPro[i]
                u1tmp += i * pixelPro[i]                          
        if w1 == 0:
            continue
        u0 = u0tmp / w0
        u1 = u1tmp / w1
        tmp_var = (float)(w0 * w1 * np.power((u0 - u1), 2))       
        if tmp_var > max_var:
            best_thresold = thresold
            max_var = tmp_var
    for x in range(height):
        for y in range(width):
            if img_array[x,y] <= best_thresold:
                   img_array[x,y]=0
            else:
                   img_array[x,y]=1    
    return best_thresold

#載入圖片
img = cv2.imread('coins.tif', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('bacteria.tif', cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread('nodules1.tif', cv2.IMREAD_GRAYSCALE)
img4 = cv2.imread('rice.tif', cv2.IMREAD_GRAYSCALE)

print(OTSU(img))
print(OTSU(img2))
print(OTSU(img3))
print(OTSU(img4))        
#顯示結果 
plt.subplot(2,2,1)          
plt.axis('off')
plt.imshow(img, cmap = 'gray')
plt.subplot(2,2,2)          
plt.axis('off')
plt.imshow(img2,cmap = 'gray')
plt.subplot(2,2,3)          
plt.axis('off')
plt.imshow(img3,cmap = 'gray')
plt.subplot(2,2,4)          
plt.axis('off')
plt.imshow(img4,cmap = 'gray')
plt.show()
