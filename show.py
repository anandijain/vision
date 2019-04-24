import cv2
import numpy as np
import time
# import pygame

# W = 1920 // 2
# H = 1080 // 2

# screen = pygame.display.set_mode((W, H))


# cv2.namedWindow('image', cv2.WINDOW_NORMAL)


if __name__ == "__main__":
    img = cv2.imread('cvtest.jpg')
    # img_cp = np.copy(cv2.resize(img, (W, H)))
    # gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # blur = cv2.GaussianBlur(gray, (11, 11), 0)
    # canny = cv2.Canny(gray, 150, 300)
    res = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
    # cv2.imwrite('output_contour.png',  canny)
    # cv2.imwrite('output_contour_resized.png',  res)
    cv2.imshow('canny', res)
    cv2.waitKey(0)

    # pygame.display.flip()
    print(img.shape)  
