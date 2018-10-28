import cv2
import numpy as np 
import math, sys
from PIL import Image

image = cv2.imread(sys.argv[1]) #reading the image
b = image.copy()
# set green and red channels to 0
b[:, :, 1] = 0
b[:, :, 2] = 0
gray = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY) # converting to grayscale image
(thresh, im_bw) = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) # converting to binary image
(_, contours, _) = cv2.findContours(~im_bw,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    cv2.drawContours(image,[contour],0,(0,0,255),2)

cv2.imshow('binary', im_bw)
cv2.imshow('gray', gray)
cv2.imshow('image', b)
cv2.imshow('image2', image)
# cv2.imwrite('test.png', image)
cv2.waitKey(0)
cv2.destroyAllWindows()