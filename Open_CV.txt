# OpenCV - Open computer vision
from google.colab import files
file = files.upload()

# Library Opency
# memanggil library opency
# baca gambar dengan pola
import cv2
# memanggil fungsi google colab untuk memperbaiki syntax menampilkan dilayar
from google.colab.patches import cv2_imshow
# membuat variabel untuk memuat nilai gambar yang ada di folder kerja
img = cv2.imread("lego2.jpg")
# menampilkan di layar dengan memanggil variabel img yang sudah berisi nilai gambar
cv2_imshow(img)
# melihat tipe data dari variabel img disimpan sebagai apa
print(type(img))

# Gambar Tepi
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("lego2.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

canny_output = cv2.Canny(image, 80, 80)

plt.subplot(121), plt.imshow(cv2.cvtColor (img, cv2.COLOR_BGR2RGB))
plt.title("gambar asli"),plt.xticks([]),plt.yticks([])
plt.subplot(122), plt.imshow(canny_output,cmap="gray")
plt.title("gambar tepi"),plt.xticks([]),plt.yticks([])
plt.show()

# Instal Rembg
pip install rembg[gpu,cli]

# Import Gambar
from rembg import remove
from PIL import Image
import cv2

# JPG ke PNG
input_path = '/content/sample_data/IMG_2352.jpg'
output_path = '/content/sample_data/IMG_2352.png'

# Menghapus bg
with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)