import os
import cv2
import time

def capture():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imwrite('/pics/frame.png', frame)
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    if not os.path.isdir('/pics/'):
        os.mkdir('/pics/')
    capture()
