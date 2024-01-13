import cv2
import numpy as np
import matplotlib.pyplot as plt

def process_image(image_path):
   
    original_image = cv2.imread(image_path)

    edges = cv2.Canny(cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY), 50, 150)
    edge_image = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)

  
    hsv = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, np.array([0, 0, 0]), np.array([20, 255, 255]))
    segmented_image = cv2.bitwise_and(original_image, original_image, mask=mask)


    plt.figure(figsize=(10, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
    plt.title('Gambar Asli')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(edge_image)
    plt.title('Deteksi Gambar')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(cv2.cvtColor(segmented_image, cv2.COLOR_BGR2RGB))
    plt.title('Segmentasi')
    plt.axis('off')

    plt.show()


process_image('apel2.jpg')
