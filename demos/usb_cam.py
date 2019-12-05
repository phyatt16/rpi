import gpiozero
import cv2

cam = cv2.VideoCapture(0)
cv2.namedWindow('RaspberryPi')

if __name__=="__main__":

    while True:

        ret,frame = cam.read()
        frame = cv2.resize(frame,(200,200))
        cv2.imshow('RaspberryPi',frame)
        k = cv2.waitKey(1)
