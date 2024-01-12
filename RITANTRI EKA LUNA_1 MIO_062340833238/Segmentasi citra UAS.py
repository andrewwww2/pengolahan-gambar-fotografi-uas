import cv2
import numpy as np
import matplotlib.pyplot as plt

def thresholding_segmentation(image_path, threshold_value):
    # Baca citra input
    input_image = cv2.imread(image_path)

    # Ubah citra ke dalam ruang warna keabuan (grayscale)
    gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

    # Lakukan thresholding pada citra untuk segmentasi
    _, thresholded_image = cv2.threshold(gray_image, threshold_value, 270, cv2.THRESH_BINARY)

    # Invert thresholded image
    inverted_threshold = cv2.bitwise_not(thresholded_image)

    # Gunakan citra hasil thresholding sebagai mask untuk mempertahankan warna asli
    result_image = cv2.bitwise_and(input_image, input_image, mask=inverted_threshold)

    # Tampilkan citra hasil segmentasi tanpa menggunakan cv2.imshow
    plt.imshow(cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB))
    plt.axis('off')  # Hilangkan sumbu x dan y
    plt.show()
--
# Baca gambar
img = cv2.imread("pisang.jpg")# Ganti 'contoh_gambar.jpg' dengan nama file gambar Anda
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
canny = cv2.Canny(img, 100, 200)

#pemberian judul gambar yang ditampilkan
titles = ['image', 'canny']
images = [img, canny]

for i in range(2):
    #Plot hasil deteksi tepi
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

#menampilkan hasil
plt.show()

# Ganti 'nama_citra_input.jpg' dengan nama file citra yang ingin Anda gunakan
# Ganti nilai threshold_value sesuai dengan nilai threshold yang diinginkan
thresholding_segmentation('pisang.jpg', 100)  # Contoh nilai threshold

