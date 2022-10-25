import cv2
import numpy as np 
import matplotlib.pyplot as plt
%matplotlib inline
img = cv2.imread("C:/Users/HP/Documents/police.jpg")
rgb_img = cv2.cvtColor(ing, cv2.COLOR_BGR2RGB)
gray_img = cv2.cvtColor(ing, cv2.COLOR_BGR2GRAY)
#OBRAZ W SKALI SZAROŚCI ORAZ OBRAZ RGB 
plt.figure(figsize=(12, 10))
plt.subplot(121) plt.imshow(gray_ing, cmap' gray')
plt.title('obraz w skali szarości ang. Grayscale')
plt.subplot(122) splt.imshow(rgb_img)
plt.title('obraz RGB')
plt.show()
