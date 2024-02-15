import cv2

# Videoaufnahme initialisieren
cap = cv2.VideoCapture(cv2.CAP_V4L2)  # Verwendung von Video4Linux2 (V4L2)
cap.set(cv2.CAP_PROP_FPS, 15)  # Einstellen der Bildrate auf 15 FPS (Frames pro Sekunde)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 160)  # Einstellen der Bildbreite auf 160 Pixel
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 120)  # Einstellen der Bildhöhe auf 120 Pixel

# Funktion zum Erfassen eines Einzelbildes
def getImg():
    _, img = cap.read()  # Einzelbild aus dem Video-Stream lesen
    return img

if __name__ == '__main__':
    while True:
        img = getImg()  # Einzelbild abrufen
        frame_rate = cap.get(cv2.CAP_PROP_FPS)  # Bildrate des Videos abrufen
        print(f'Die Bildrate des Videos beträgt: {frame_rate} FPS')
        # Hier könntest du das Einzelbild weiterverarbeiten oder anzeigen
        # Zum Anzeigen des Einzelbildes den Kommentarzeichen (#) in den folgenden Zeilen entfernen:
        # cv2.imshow('Result', img)
        # key = cv2.waitKey(1)
