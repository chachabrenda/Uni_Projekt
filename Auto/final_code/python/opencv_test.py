import cv2
from picamera2 import Picamera2

# Picamera2-Objekt erstellen
picam2 = Picamera2()

# Vorschau-Konfiguration festlegen (Größe und Format)
picam2.preview_configuration.main.size = (640, 480)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()

# Vorschau konfigurieren und starten
picam2.configure("preview")
picam2.start()

while True:
    # Einzelbild von der Kamera erfassen
    img = picam2.capture_array()
    
    # Bild anzeigen
    cv2.imshow('img', img)
    
    # Bild filtern (Canny-Filter)
    filtered = cv2.Canny(img, 100, 300)
    
    # Gefiltertes Bild anzeigen
    cv2.imshow('filtered', filtered)
    
    # Auf Tastatureingabe warten (10 ms)
    cv2.waitKey(10)
