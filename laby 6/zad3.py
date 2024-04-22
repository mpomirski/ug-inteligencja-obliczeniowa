import cv2
import numpy as np
import os

images = os.listdir('bird_miniatures')
for image_name in images:
    image = cv2.imread('bird_miniatures/' + image_name)
    # Convert to grayscale
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Make it a little bigger
    image = cv2.resize(image, (200, 200))
    # Apply Thresholding
    image = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
    cv2.THRESH_BINARY,11,2)
    # Dilate the image (make the birds bigger)
    image = cv2.dilate(image, np.ones((2, 2), np.uint8), iterations=1)
    # Find contours
    contours = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
    s1 = 8
    s2 = 1000
    xcnts = []
    # Take only the contours with an s1 <= area <= s2
    for cnt in contours:
        if cv2.contourArea(cnt) > s1 and cv2.contourArea(cnt) < s2:
            xcnts.append(cnt)
    print(f'{image_name}: {len(xcnts)} birds.')