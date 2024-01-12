import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("baygon.jpeg")

edge = cv2.Canny(img,100,200)

plt.subplot(121), plt.imshow(img, cmap="gray")
plt.title("gambar asli"),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(edge,cmap="gray")
plt.title("gambar tepi"),plt.xticks([]),plt.yticks([])
plt.show()