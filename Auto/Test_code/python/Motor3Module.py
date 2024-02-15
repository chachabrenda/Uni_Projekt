import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
class Motor():
    def __init__(self,EnaA,In1A,In2A,EnaB,In1B,In2B,EnaC,In1C,In2C):
        self.EnaA = EnaA
        self.In1A = In1A
        self.In2A = In2A
        self.EnaB = EnaB
        self.In1B = In1B
        self.In2B = In2B
        self.EnaC = EnaC
        self.In1C = In1C
        self.In2C = In2C
        GPIO.setup(self.EnaA,GPIO.OUT)
        GPIO.setup(self.In1A,GPIO.OUT)
        GPIO.setup(self.In2A,GPIO.OUT)
        GPIO.setup(self.EnaB,GPIO.OUT)
        GPIO.setup(self.In1B,GPIO.OUT)
        GPIO.setup(self.In2B,GPIO.OUT)
        GPIO.setup(self.EnaC,GPIO.OUT)
        GPIO.setup(self.In1C,GPIO.OUT)
        GPIO.setup(self.In2C,GPIO.OUT)
        self.pwmA = GPIO.PWM(self.EnaA, 100);
        self.pwmA.start(0);
        self.pwmB = GPIO.PWM(self.EnaB, 100);
        self.pwmB.start(0);
        self.pwmC = GPIO.PWM(self.EnaC, 100);
        self.pwmC.start(0);
 
    def move(self,speed=0.5,turn=0,t=0):
        speed *=100
        turn *=100
 
        self.pwmA.ChangeDutyCycle(abs(speed))
        self.pwmB.ChangeDutyCycle(abs(speed))
        self.pwmC.ChangeDutyCycle(abs(turn))
 
        if speed > 0:
           GPIO.output(self.In1A, GPIO.HIGH)
           GPIO.output(self.In2A, GPIO.LOW)
           GPIO.output(self.In1B, GPIO.LOW)
           GPIO.output(self.In2B, GPIO.HIGH)
        elif speed < 0:
           GPIO.output(self.In1A, GPIO.LOW)
           GPIO.output(self.In2A, GPIO.HIGH)
           GPIO.output(self.In1B, GPIO.HIGH)
           GPIO.output(self.In2B, GPIO.LOW)

        if turn > 0:
           GPIO.output(self.In1C, GPIO.HIGH)
           GPIO.output(self.In2C, GPIO.LOW)
           self.pwmA.ChangeDutyCycle(abs(turn))
           GPIO.output(self.In1A, GPIO.HIGH)
           GPIO.output(self.In2A, GPIO.LOW)
           self.pwmB.ChangeDutyCycle(abs(turn))
           GPIO.output(self.In1B, GPIO.HIGH)
           GPIO.output(self.In2B, GPIO.LOW)
        elif turn < 0:
           GPIO.output(self.In1C, GPIO.LOW)
           GPIO.output(self.In2C, GPIO.HIGH)
           self.pwmA.ChangeDutyCycle(abs(turn))
           GPIO.output(self.In1A, GPIO.LOW)
           GPIO.output(self.In2A, GPIO.HIGH)
           self.pwmB.ChangeDutyCycle(abs(turn))
           GPIO.output(self.In1B, GPIO.LOW)
           GPIO.output(self.In2B, GPIO.HIGH)
           

 
        sleep(t)
    def stop(self,t=0):
        self.pwmA.ChangeDutyCycle(0);
        self.pwmB.ChangeDutyCycle(0);
        self.pwmC.ChangeDutyCycle(0);
        sleep(t)
 
 
def main():
    motor.move(0.4,0.2,2)
    motor.stop(2)
    motor.move(-0.3,-0.2,2)
    motor.stop(2)
 
if __name__ == '__main__':
    motor = Motor(10, 9, 11, 17, 22, 27, 14, 15, 18)
    main()
