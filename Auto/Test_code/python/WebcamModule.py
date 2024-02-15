import cv2

cap = cv2.VideoCapture(cv2.CAP_V4L2)
cap.set(cv2.CAP_PROP_FPS, 15)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 160)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 120)

def getImg():
    _, img = cap.read()
    return img

if __name__ == '__main__':
    while True:
        img = getImg()
        # get the frame rate of the video
        frame_rate = cap.get(cv2.CAP_PROP_FPS)
        print(f'The frame rate of the video is: {frame_rate} FPS')
        #cv2.imshow('Result', img)
        #key = cv2.waitKey(1)

