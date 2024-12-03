import threading
import time

class Calculator : 
    number = ''
    def __init__(self, number):
        self.Number = number

    def runCal(self) :
        hap=0
        for i in range(0,self.Number+1) :
            hap += i
        print("1+2+3+.....+",self.Number,"=",hap)

cal1 = Calculator(1000)
cal2 = Calculator(100000)
cal3 = Calculator(10000000)

th1 = threading.Thread(target=cal1.runCal)
th2 = threading.Thread(target=cal2.runCal)
th3 = threading.Thread(target=cal3.runCal)

th1.start()
th2.start()
th3.start()
