import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("pisang.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

canny_output = cv2.Canny(image, 80, 80)

plt.subplot(121), plt.imshow(cv2.cvtColor (img, cv2.COLOR_BGR2RGB))
plt.title("gambar asli"),plt.xticks([]),plt.yticks([])
plt.subplot(122), plt.imshow(canny_output,cmap="gray")
plt.title("gambar tepi"),plt.xticks([]),plt.yticks([])
plt.show()