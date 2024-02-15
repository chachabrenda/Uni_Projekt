import cv2

from picamera2 import Picamera2
picam2 = Picamera2()
picam2.preview_configuration.main.size = (640,480)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()

while True:
    img = picam2.capture_array()
    cv2.imshow('img', img)
    filtered = cv2.Canny(img, 100, 300)
    cv2.imshow('filtered', filtered)
    cv2.waitKey(10)

