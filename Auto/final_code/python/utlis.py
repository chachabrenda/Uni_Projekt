# Importieren der erforderlichen Module
import cv2
import numpy as np

# Funktion zur Schwellenwertbildung (Thresholding) des Bildes
def thresholding(img):
    # Konvertiere das Bild in Graustufen
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Führe eine Gauß'sche Unschärfe auf dem Graustufenbild durch
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 0)
    # Verwende den OTSU-Schwellenwert und erzeuge ein invertiertes Binärbild
    _, imgThresh = cv2.threshold(imgBlur, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    return imgThresh

# Funktion zur perspektivischen Transformation des Bildes
def warpImg(img, points, w, h, inv=False):
    # Definiere die Koordinaten der Ecken im Eingangsbild und im Ausgabebild
    pts1 = np.float32(points)
    pts2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
    # Berechne die Transformationsmatrix basierend auf den Punkten
    if inv:
        matrix = cv2.getPerspectiveTransform(pts2, pts1)
    else:
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
    # Führe die perspektivische Transformation durch
    imgWarp = cv2.warpPerspective(img, matrix, (w, h))
    return imgWarp

# Leere Funktion zur Verwendung mit Trackbars (falls erforderlich)
def nothing(a):
    pass

# Funktion zur Initialisierung der Trackbars für die Bildtransformation
def initializeTrackbars(intialTracbarVals, wT=160, hT=120):
    # Erstelle ein Fenster für die Trackbars
    cv2.namedWindow("Trackbars")
    # Ändere die Größe des Fensters
    cv2.resizeWindow("Trackbars", 300, 180)
    # Erstelle Trackbars für die Parameter der perspektivischen Transformation
    cv2.createTrackbar("Width Top", "Trackbars", intialTracbarVals[0], wT // 2, nothing)
    cv2.createTrackbar("Height Top", "Trackbars", intialTracbarVals[1], hT, nothing)
    cv2.createTrackbar("Width Bottom", "Trackbars", intialTracbarVals[2], wT // 2, nothing)
    cv2.createTrackbar("Height Bottom", "Trackbars", intialTracbarVals[3], hT, nothing)

# Funktion zum Abrufen der aktuellen Trackbar-Werte
def valTrackbars(wT=160, hT=120):
    widthTop = 36   
    heightTop = 56
    widthBottom = 7
    heightBottom = 94
    # Definiere die Punkte für die perspektivische Transformation basierend auf den Trackbar-Werten
    points = np.float32([(widthTop, heightTop), (wT - widthTop, heightTop),
                         (widthBottom, heightBottom), (wT - widthBottom, heightBottom)])
    return points

# Funktion zum Zeichnen von Punkten auf einem Bild
def drawPoints(img, points):
    for x in range(4):
        cv2.circle(img, (int(points[x][0]), int(points[x][1])), 15, (0, 0, 255), cv2.FILLED)
    return img

# Funktion zur Erstellung eines Histogramms für ein Bild
def getHistogram(img, display=True, minPer=0.1, region=1):
    if region == 1:
        histValues = np.sum(img, axis=0)
    else:
        histValues = np.sum(img[img.shape[0] // region:, :], axis=0)
    maxValue = np.max(histValues)
    minValue = minPer * maxValue

    indexArray = np.where(histValues >= minValue)
    basePoint = int(np.average(indexArray))
    imgHist = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)

    for x, intensity in enumerate(histValues):
        cv2.line(imgHist, (x, img.shape[0]), (x, img.shape[0] - intensity // 255 // region), (255, 0, 255), 1)
        cv2.circle(imgHist, (basePoint, img.shape[0]), 20, (0, 255, 255), cv2.FILLED)
    return basePoint, imgHist

# Funktion zum Stapeln von Bildern horizontal oder vertikal
def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver
