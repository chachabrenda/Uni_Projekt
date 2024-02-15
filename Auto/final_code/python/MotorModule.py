import RPi.GPIO as GPIO
from time import sleep

# GPIO-Initialisierung
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Klasse zur Steuerung des Motors
class Motor():
    def __init__(self, EnaA, In1A, In2A, EnaB, In1B, In2B):
        # GPIO-Pins für die Motorsteuerung
        self.EnaA = EnaA
        self.In1A = In1A
        self.In2A = In2A
        self.EnaB = EnaB
        self.In1B = In1B
        self.In2B = In2B
        
        # GPIO-Pins als Ausgang initialisieren
        GPIO.setup(self.EnaA, GPIO.OUT)
        GPIO.setup(self.In1A, GPIO.OUT)
        GPIO.setup(self.In2A, GPIO.OUT)
        GPIO.setup(self.EnaB, GPIO.OUT)
        GPIO.setup(self.In1B, GPIO.OUT)
        GPIO.setup(self.In2B, GPIO.OUT)
        
        # PWM-Objekte für die Motoren erstellen und starten
        self.pwmA = GPIO.PWM(self.EnaA, 100)
        self.pwmB = GPIO.PWM(self.EnaB, 100)
        self.pwmA.start(0)
        self.pwmB.start(0)
        self.mySpeed = 0
 
    def move(self, speed=0.5, turn=0, t=0):
        # Geschwindigkeit und Lenkwinkel in PWM-Duty-Cycle-Werte umrechnen
        speed *= 100
        turn *= 80
        leftSpeed = speed - turn
        rightSpeed = speed + turn
        
        # Begrenze die PWM-Duty-Cycle-Werte auf den Bereich [-100, 100]
        if leftSpeed > 100: leftSpeed = 100
        elif leftSpeed < -100: leftSpeed = -100
        if rightSpeed > 100: rightSpeed = 100
        elif rightSpeed < -100: rightSpeed = -100
        
        # PWM-Duty-Cycle für die Motoren setzen
        self.pwmA.ChangeDutyCycle(abs(leftSpeed))
        self.pwmB.ChangeDutyCycle(abs(rightSpeed))
        
        # Motorrichtungen entsprechend der Geschwindigkeit einstellen
        if leftSpeed > 0:
            GPIO.output(self.In1A, GPIO.HIGH)
            GPIO.output(self.In2A, GPIO.LOW)
        else:
            GPIO.output(self.In1A, GPIO.LOW)
            GPIO.output(self.In2A, GPIO.HIGH)
        
        if rightSpeed > 0:
            GPIO.output(self.In1B, GPIO.HIGH)
            GPIO.output(self.In2B, GPIO.LOW)
        else:
            GPIO.output(self.In1B, GPIO.LOW)
            GPIO.output(self.In2B, GPIO.HIGH)
        
        sleep(t)
 
    def stop(self, t=0):
        # Alle Motoren stoppen
        self.pwmA.ChangeDutyCycle(0)
        self.pwmB.ChangeDutyCycle(0)
        self.mySpeed = 0
        sleep(t)
 
def main():
    # Verschiedene Bewegungen ausführen und dann anhalten
    motor.move(0.5, 0, 2)  # Vorwärts
    motor.stop(2)
    motor.move(-0.5, 0, 2)  # Rückwärts
    motor.stop(2)
    motor.move(0, 0.5, 2)  # Rechts drehen
    motor.stop(2)
    motor.move(0, -0.5, 2)  # Links drehen
    motor.stop(2)
 
if __name__ == '__main__':
    # Motorinstanz erstellen und Hauptfunktion aufrufen
    motor = Motor(10, 9, 11, 17, 27, 22)
    main()
