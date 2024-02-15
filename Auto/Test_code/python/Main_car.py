
import pygame
from MotorModule import Motor
import os
from LaneModule import getLaneCurve
import WebcamModule
import cv2
import time

os.environ["SDL_VIDEODRIVER"] = "dummy"
pygame.init()

# Initialize the joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()

motor = Motor(10, 11, 9, 17, 22, 27)

# Previous joystick values
prev_x, prev_y = joystick.get_axis(0), joystick.get_axis(1)

activate = False


# Main Loop
while True:
    img = WebcamModule.getImg()
    curveVal= getLaneCurve(img, 0)
    print("button 0 down")
    print("original Value -----------> : ")
    print(curveVal)
    maxVAl= 0.02 # MAX SPEED
    if curveVal>maxVAl:curveVal = maxVAl
    if curveVal<-maxVAl: curveVal =-maxVAl
    if activate:
        motor.move(0.06, curveVal, 0.01)
    # Check for joystick events
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:                
                print("autopilot activated")
                activate = not activate
            elif event.button == 1:
                print("button 1 down")
                #rotate 180 degrees
                motor.move(0, 0.4, 2)
                motor.stop(1)

    # Check the joystick's axis values
    x, y = joystick.get_axis(0), joystick.get_axis(1)
    if x != prev_x or y != prev_y:
        print(f"Joystick values: x={x}, y={-y}")
        motor.move(-y*0.7, x*0.5, 0.1)
        # Update previous joystick values
        prev_x, prev_y = x, y
