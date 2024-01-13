import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("buah.jpg")
edge = cv2.Canny(img,50,100) #melakukan deteksi tepi

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #menentukan jenis warna 
lower = np.array([20, 50, 20]) #menentukan ambang batas bawah warna 
higher = np.array([100, 255, 255]) #menentukan ambang batas atas 
mask = cv2.inRange(hsv, lower, higher) #membuat masking untuk mencari objek sesuai batas warna 
    
result = cv2.bitwise_and(img, img, mask=mask) 

#proses untuk menampilkan gambar 
plt.subplot(141), plt.imshow(cv2.cvtColor (img, cv2.COLOR_BGR2RGB))
plt.title("gambar asli"),plt.xticks([]),plt.yticks([]) #menampilkan gambar asli
plt.subplot(142), plt.imshow (cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
plt.title("gambar gray"),plt.xticks([]),plt.yticks([]) #menampilkan gambar abu
plt.subplot(143),plt.imshow(edge, cmap="gray")
plt.title("gambar tepi"),plt.xticks([]),plt.yticks([]) #menampilkan deteksi tepi
plt.subplot(144), plt.imshow(cv2.cvtColor (result, cv2.COLOR_BGR2RGB))
plt.title("hasil segmentasi"),plt.xticks([]),plt.yticks([]) #menampilkan segmentasi
plt.show()