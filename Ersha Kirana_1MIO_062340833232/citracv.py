# Import library yang diperlukan.
import cv2
import numpy as np

# Membaca file citra, lalu disimpan kedalam variabel "citra".
citra = cv2.imread("kafe.jpg")

# Menggunakan metode Canny Edge Detection untuk menghilangkan Noise dengan metode Gaussian Smoothing, dan menerapkan
# threshold dengan 2 threshold values yang dimasukkan sebagai argumen kedalam method cv2.Canny().
tepi_citra = cv2.Canny(citra, 100, 300)

# Mengkonversi citra dari RGB ke HSV.
citraInHSV = cv2.cvtColor(citra, cv2.COLOR_BGR2HSV)

# Menentukan batas minimal threshold.
lower_b = np.array([0, 0, 30])

# Menentukan batas maksimal threshold.
upper_b = np.array([200, 60, 300])

# Membuat mask citra menggunakan method inRange(), dengan variabel "lower_b" sebagai batas minimal threshold dan
# variabel "upper_b" sebagai batas maksimal threshold.
mask_citra = cv2.inRange(citraInHSV, lower_b, upper_b)

# Memisahkan objek dari background dalam citra menggunakan method bitwise_and() dengan bantuan masking dari "mask_citra"
citra_segmentasi = cv2.bitwise_and(citra, citra, mask=~mask_citra)

# Menampilkan Citra asli, Citra deteksi tepi dan Citra hasil segmentasi
cv2.imshow('Gambar asli', citra)
cv2.imshow('Citra deteksi tepi', tepi_citra)
cv2.imshow('Citra hasil segmentasi', citra_segmentasi)

cv2.waitKey(0)
cv2.destroyAllWindows()
