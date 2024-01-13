# Kode ini untuk menginstall rembg, ini wajib dilakukan dan haous komentar ini ketika dijalankan karena suka error
 

pip install rembg[gpu,cli]

# Pada bagian ini adalah program yang berisi perintah untuk menampilkan output upload files jika menggunakan google colab dan bisa juga menggunakan cara manual
from google.colab import files
file = files.upload()


# Pada baris kode ini berfungsi untuk mengimpor modul "rembg" untuk melakkukan proses segmentasi menghaps background
from rembg import remove

# Kemudian pada baris kode ini berfungsi untuk mengimpor modul "PIL" untuk manipulasi gambar
from PIL import Image, ImageOps, ImageFilter

# Lalu pada baris kode ini berfungsi untuk mengimpor "io" untuk operasi input/output byte
import io

# Terakhir ada modeul "matplotlib.pyplot" untuk menampilkan gambar
import matplotlib.pyplot as plt

# Pada baris kode ini menentukan path gambar input dan path gambar output untuk citra grayscale, deteksi tepi, dan hasil segmentasi
input_path = '/content/IMG_20240112_073335.jpg'
output_path_grayscale = '/content/grayscale.png'
output_path_edges = '/content/deteksi_tepi.png'
output_path_removed_bg = '/content/segmentasi.png'

# Pada bagian ini membaca gambar asli dari path yang telah ditentukan
with open(input_path, 'rb') as i:   # Membuka file gambar dalam mode baca binary
    input_data = i.read()    # Membaca data gambar sebagai byte
    original_image = Image.open(io.BytesIO(input_data))    # Membaca gambar dari data byte menggunakan modul "PIL"

# Kode ini mengonversi gambar asli ke citra grayscale menggunakan fungsi "ImageOps.grayscale"
# Hasilnya disimpan sebagai file gambar grayscale dengan path yang telah ditentukan
grayscale_image = ImageOps.grayscale(original_image)
grayscale_image.save(output_path_grayscale)

# Pada kode ini metode deteksi tepi dengan menggunakan filter ImageFilter.FIND_EDGES pada citra grayscale
# Hasilnya nanti akan disimpan sebagai file gambar dengan deteksi tepi di output_path_edges
edges_image = grayscale_image.filter(ImageFilter.FIND_EDGES)
edges_image.save(output_path_edges)

# Pada baris kode ini saya menggunakan library "rembg" untuk menghapus latar belakang dari gambar asli
# Dan kemudian hasilnya akan disimpan sebagai file gambar dengan latar belakang yang sudah disegmentasi di output_path_removed_bg
output_data = remove(input_data)
removed_bg_image = Image.open(io.BytesIO(output_data))
removed_bg_image.save(output_path_removed_bg)

# Pada baris kode ini berfungsi agar menampilkan hasil gambar yang kita inginkan secara langsung
plt.figure(figsize=(12, 8))

# Ini adalah kode untuk menampilkan gambar asli dari yang diupload
# Kode ini juga menggunakan Matplotlib untuk menampilkan keempat gambar di bawah kode
plt.subplot(221)    # Ini digunakan untuk menentukan layout gambar dan judulnya
plt.imshow(original_image)    # Ini digunakan untuk menampilkan gambar
plt.title('Gambar Asli')    # Ini digunakan untuk memberikan judul pada gambar
plt.axis('off')    # Ini digunakan untuk menyembunyikan sumbu pada setiap gambar

# Pada kode ini berfungsi untuk menampilkan gambar yang sudah menjadi citra grayscale
plt.subplot(222)
plt.imshow(grayscale_image, cmap='gray')
plt.title('Citra Grayscale')
plt.axis('off')

# Pada kode ini berfungsi untuk menampilkan gambar yang sudah di deteksi tepi dari yang sebelumnya citra grayscale
plt.subplot(223)
plt.imshow(edges_image, cmap='gray')
plt.title('Citra deteksi tepi')
plt.axis('off')

# Pada kode ini berfungsi untuk menampilkan gambar yang sudah disegmentasi atau dihilangkan latar belakangnya
plt.subplot(224)
plt.imshow(removed_bg_image)
plt.title('Citra hasil segmentasi')
plt.axis('off')

# Terakhir pada baris kode ini berfungsi untuk memunculkan jendela plot atau gambar sehingga dapat dilihat atau disimpan oleh pengguna
plt.show()
