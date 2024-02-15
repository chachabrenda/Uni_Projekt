# Importieren der erforderlichen Module
from MotorModule import Motor
from LaneModule import getLaneCurve
import WebcamModule
import time
import psutil
import os

# Setzen der Umgebungsvariable für das SDL-Video auf "dummy" (headless-Modus)
os.environ["SDL_VIDEODRIVER"] = "dummy"

# Initialisierung des Motors mit den entsprechenden GPIO-Pins
motor = Motor(10, 11, 9, 17, 22, 27)

# Aktuelle Prozess-ID und CPU-Auslastung abrufen
pid = os.getpid()
py = psutil.Process(pid)
cpu_use = py.cpu_percent(interval=1)

# Hauptfunktion
def main():
    start_time = time.time()
    
    # Speichernutzung in GB anzeigen
    memoryUse = py.memory_info()[0] / 2.0**30  # Speichernutzung in GB...
    print('Speichernutzung:', memoryUse, 'GB')
    
    # Einzelbild von der Webcam erfassen
    img = WebcamModule.getImg()
    
    # Fahrspurkurve bestimmen
    curveVal = getLaneCurve(img, 0)
    
    # Maximalgeschwindigkeit und Kurvenempfindlichkeit festlegen
    maxVal = 0.03  # Maximale Geschwindigkeit
    if curveVal > maxVal:
        curveVal = maxVal
    if curveVal < -maxVal:
        curveVal = -maxVal
    
    # Motorbewegung basierend auf der Kurve ausführen
    motor.move(0.06, curveVal, 0.01)
    
    # CPU-Auslastung anzeigen
    print("CPU-Auslastung: " + str(psutil.cpu_percent()) + "%")
    
    end_time = time.time()
    execution_time = end_time - start_time
    print(f'Ausführungszeit: {execution_time} Sekunden')

if __name__ == '__main__':
    while True:
        main()
