import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_image(image, title):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Fungsi untuk melakukan deteksi tepi pada gambar
def edge_detection(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    return cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)

# Fungsi untuk melakukan segmentasi (hapus background) pada gambar dengan latar belakang putih
def remove_background(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 0, 200])  # Nilai batas bawah untuk warna merah dalam format HSV
    upper_red = np.array([10, 50, 255])  # Nilai batas atas untuk warna merah dalam format HSV
    mask = cv2.inRange(hsv, lower_red, upper_red)
    
    # Segmentasi dengan mengganti warna background menjadi putih
    result = np.ones_like(image) * 255
    result[mask == 0] = image[mask == 0]
    
    return result

# Baca gambar asli
original_image = cv2.imread('mobil.jpg')

# Deteksi tepi pada gambar
edge_image = edge_detection(original_image)

# Hapus background pada gambar dengan segmentasi warna putih
segmented_image = remove_background(original_image)

# Tampilkan ketiga gambar dalam satu jendela
plt.figure(figsize=(10, 5))

# Gambar asli
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
plt.title('Gambar Asli')
plt.axis('off')

# Gambar dengan deteksi tepi
plt.subplot(1, 3, 2)
plt.imshow(edge_image)
plt.title('Deteksi Gambar')
plt.axis('off')

# Gambar dengan segmentasi background putih
plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(segmented_image, cv2.COLOR_BGR2RGB))
plt.title('Segmentasi Background Putih')
plt.axis('off')

# Tampilkan jendela
plt.show()
