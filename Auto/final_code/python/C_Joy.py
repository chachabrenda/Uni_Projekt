import pygame
from MotorModule_new import Motor

pygame.init()

# Initialize the joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Xbox Joystick Axis:
# Axis 0 up down, down value is -1, up value is 1
# Axis 1 Left, Right, Left value is: -1, right value is 1
# center is always 0

##################
motor = Motor(2, 3, 4, 17, 22, 27, 14, 15, 18)

# Previous joystick values
prev_x, prev_y = joystick.get_axis(0), joystick.get_axis(1)

# Main Loop
while True:
    # Check for joystick events
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:
                print("button 0 down")
                motor.move(0.6, 0, 0.1)
            elif event.button == 1:
                print("button 1 down")
                motor.move(-0.6, 0, 0.1)
            elif event.button == 2:
                print("button 2 down")
                motor.move(0, -0.8, 0.1)
            elif event.button == 3:
                print("button 3 down")
                motor.move(0, 0.8, 0.1)
            elif event.button == 5:
                print("button 5 down")
            elif event.button == 6:
                print("button 6 down")
            elif event.button == 7:
                print("button 7 down")
            elif event.button == 8:
                print("button 8 down")

    # Check the joystick's axis values
    x, y = joystick.get_axis(0), joystick.get_axis(1)
    if x != prev_x or y != prev_y:
        print(f"Joystick values: x={x}, y={y}")
        # Move the motors according to the joystick's axis values
        motor.move(y * 0.8, x * 0.6, 0.1)

        # Update previous joystick values
        prev_x, prev_y = x, y

