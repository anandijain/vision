import cv2
import numpy as np
import time

PATH = 'images/cvtest.jpg'


if __name__ == "__main__":
    img = cv2.imread('images/cvtest.jpg')
    res = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)

    cv2.imshow('resized', res)
    cv2.waitKey(0)

    print(img.shape)  
