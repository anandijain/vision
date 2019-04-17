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
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)
    cv2.imwrite('output_contour.png',  canny)
    cv2.imshow('canny', canny)
    cv2.waitKey(0)

    # pygame.display.flip()
    print(img.shape)  
