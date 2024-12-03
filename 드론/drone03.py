#지그재그
from time import *
from e_drone.drone import *
from e_drone.protocol import *

if __name__ == '__main__' :
    drone = Drone()
    drone.open("COM8")
    print("TakeOff")
    drone.sendTakeOff()
    sleep(0.01)

    print("Hovering")
    drone.sendControlWhile(0,0,0,0,4000)

    print("Right Turn")
    drone.sendControlWhile(0,0,-30,0,600)

    print("Zigzag")
    for i in range(4,0,-1) :
        drone.sendControlWhile(0, 60, 0, 0, 1000)
        drone.sendControlWhile(0, 0, 60, 0, 600)
        drone.sendControlWhile(0, 60, 0, 0, 1000)
        drone.sendControlWhile(0, 0, -60, 0, 600)

    print("left turn")
    drone.sendControlWhile(0, 0, 30, 0, 600)

    print("Go Stop")
    drone.sendControlWhile(0, 0, 0, 0, 1000)
    print("Landing")

    drone.sendLanding()
    sleep(0.01)
    drone.sendLanding()
    sleep(0.01)

    drone.close()