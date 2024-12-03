#마름모
from time import *
from e_drone.drone import *
from e_drone.protocol import *

if __name__ == '__main__' :
    drone = Drone()
    drone.open("COM8")
    print("TakeOff")
    drone.sendTakeOff()
    sleep(0.01)

    # 앞으로 2초 전진하면서 상승
    print("Hovering")
    drone.sendControlWhile(0,50,0,0,2000)

    #앞으로 전진
    drone.sendControlWhile(0, 50, 0, 0, 2000)
    #뒤로 후진하면서 하강 2초
    drone.sendControlWhile(0, -50, 0, -50, 2000)
    #후진 2초
    drone.sendControlWhile(0, -50, 0, 0, 2000)

    print("Go Stop")
    drone.sendControlWhile(0, 0, 0, 0, 1000)
    print("Landing")

    drone.sendLanding()
    sleep(0.01)
    drone.sendLanding()
    sleep(0.01)

    drone.close()