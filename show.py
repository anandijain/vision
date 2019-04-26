import cv2
import numpy as np
import time

IMG_PATH = 'images/cvtest.jpg'
VID_PATH = 'images/nba.mp4'

W = 1920
H = 1080

def process_frame(img):
    res = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gray, 25, 1, 10)
    corners = np.int0(corners)

    for i in corners:
        x,y = i.ravel()
        res = cv2.circle(img, (x,y), 10, 255, -1)

    cv2.imshow('img', res)
    print(res.shape)


if __name__ == "__main__":
    # img = cv2.imread('images/cvtest.jpg')
    cap = cv2.VideoCapture(VID_PATH)

    while cap.isOpened():
        ret, frame = cap.read()
        cv2.waitKey(0)
        if ret == True:
            process_frame(frame)
        else:
            break
     