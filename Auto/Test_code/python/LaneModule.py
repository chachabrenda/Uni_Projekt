import cv2
import numpy as np
import utlis
import WebcamModule
from MotorModule import Motor
import os


os.environ["SDL_VIDEODRIVER"] = "dummy"

curveList = []
avgVal = 10

def getLaneCurve(img, display):
    imgCopy = img.copy()
    imgThres = utlis.thresholding(img)
    hT, wT, c = img.shape
    points = utlis.valTrackbars()
    imgWarp = utlis.warpImg(imgThres, points, wT, hT)
    middlePoint, imgHist = utlis.getHistogram(imgWarp, minPer=0.5, region=4)
    curveAveragePoint, imgHist = utlis.getHistogram(imgWarp, minPer=0.9)
    curveRaw = curveAveragePoint - middlePoint
    curveList.append(curveRaw)
    if len(curveList) > avgVal:
        curveList.pop(0)
    curve = int(sum(curveList) / len(curveList))
    curve = curve / 100
    if curve > 1:
        curve = 1
    if curve < -1:
        curve = -1
    if display == 1:
        imgResult = img.copy()
        imgInvWarp = utlis.warpImg(imgWarp, points, wT, hT, inv=True)
        imgInvWarp = cv2.cvtColor(imgInvWarp, cv2.COLOR_GRAY2BGR)
        imgInvWarp[0:hT // 3, 0:wT] = 0, 0, 0
        imgLaneColor = np.zeros_like(img)
        imgLaneColor[:] = 0, 0, 255  # Blue color for the lane line
        imgLaneColor = cv2.bitwise_and(imgInvWarp, imgLaneColor)
        imgResult = cv2.addWeighted(imgResult, 1, imgLaneColor, 1, 0)
        midY = hT
        cv2.putText(imgResult, str(curve), (wT // 2 - 80, 85), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 255), 3)
        cv2.line(imgResult, (wT // 2, midY), (int(wT // 2 + (curve * 3)), midY), (0, 0, 255), 5)  # Blue color for the line
        cv2.line(imgResult, (int(wT // 2 + (curve * 3)), midY - 25), (int(wT // 2 + (curve * 3)), midY + 25), (255, 0, 0), 5)  # Red color for the boundary
        for x in range(-30, 30):
           w = wT // 20
           cv2.line(imgResult, (w * x + int(curve // 50), midY - 10), (w * x + int(curve // 50), midY + 10), (255, 0, 0), 2)  # Red color for the lines
        cv2.imshow('Result', imgResult)
        key = cv2.waitKey(1)
    elif display == 2:
        imgWarpPoints = utlis.drawPoints(imgCopy, points)
        imgStacked = utlis.stackImages(0.7, ([img, imgWarpPoints, imgWarp]))
        cv2.imshow('ImageStack', imgStacked)
        key = cv2.waitKey(1)
    return curve


if __name__ == '__main__':
    intialTrackBarVals = [36, 56, 7, 94]
    utlis.initializeTrackbars(intialTrackBarVals)
    
    while True:
        img = WebcamModule.getImg()
        curve = getLaneCurve(img, 0)
        print(curve)
