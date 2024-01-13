import cv2 
import numpy as np
from matplotlib import pyplot as plt

# function to perform edge detection on the image 
def edge_detection(image):
 gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 edges = cv2.Canny(gray, 50, 150)
 return cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)

# function to remove the background from the image 
def remove_background(image): 
 hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
 lower_orange = np.array([0, 100, 45])
 upper_orange = np.array([225, 250, 255])
 mask = cv2.inRange(hsv, lower_orange, upper_orange)
 result = cv2.bitwise_and(image, image, mask = mask)
 return result

# load the original image 
original_image = cv2.imread('Bunga.jpg')

# perform edge detection on the image 
edge_image = edge_detection(original_image)

# remove the background from the image 
segmented_image = remove_background(original_image)

# display the three images in one window 
plt.figure(figsize=(10, 5))

# original image 
plt.subplot(1, 3, 1) 
plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
plt.title("original image")
plt.axis("off")

# image with edges detected 
plt.subplot(1, 3, 2) 
plt.imshow(edge_image)
plt.title("edge detected image")
plt.axis("off")

# segmented image with background removed 
plt.subplot(1, 3, 3) 
plt.imshow(cv2.cvtColor(segmented_image, cv2.COLOR_BGR2RGB))
plt.title("segmented image")
plt.axis("off")

plt.show()