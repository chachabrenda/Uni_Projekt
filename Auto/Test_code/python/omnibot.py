from MotorModule import Motor
from LaneModule import getLaneCurve
import WebcamModule
import time
import psutil
import os


os.environ["SDL_VIDEODRIVER"] = "dummy"
##################################################
motor = Motor(10, 11, 9, 17, 22, 27)
##################################################
pid = os.getpid()
py = psutil.Process(pid)
cpu_use = py.cpu_percent(interval=1)
##################################################


def main():
    start_time = time.time() 
    memoryUse = py.memory_info()[0]/2.**30  # memory use in GB...
    print('Memory use:', memoryUse, 'GB')
    img = WebcamModule.getImg()
    curveVal= getLaneCurve(img, 0)
    #print("original Value -----------> : ")
    #print(curveVal)
    #sen = 1  # SENSITIVITY
    maxVAl= 0.03 # MAX SPEED
    if curveVal>maxVAl:curveVal = maxVAl
    if curveVal<-maxVAl: curveVal =-maxVAl
    #print("converted Value -----------> : ")
    #print(curveVal)
    #if curveVal>0:
    #    if curveVal<0.05: curveVal=0
    #else:
    #    if curveVal>-0.05: curveVal=0
    motor.move(0.06, curveVal, 0.01)
    #cv2.imshow("Image", img)
    #cv2.waitKey(1)
    print("CPU Util:" + str(psutil.cpu_percent()) + "%")
    end_time = time.time()
    execution_time = end_time - start_time
    print(f'Time taken: {execution_time} seconds')

if __name__ == '__main__':
    while True:
        main()
