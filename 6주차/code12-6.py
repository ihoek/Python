## 클래스 선언 부분 ##
class Car : 
    color = ""
    speed = 0
    count = 0

    def __init__(self) :
        self.speed = 0
        Car.count += 1


## 변수 선언 부분 ##
myCar1, myCar2 = None, None

## 메인 코드 부분 ##
myCar1 = Car()
myCar1.speed = 30
print("자동차1의 속도는 %dkm이며, 생산된 자동차는 %d대입니다." % (myCar1.speed, Car.count))

myCar2 = Car()
myCar2.speed = 60
print("자동차2의 속도는 %dkm이며, 생산된 자동차는 %d대입니다." % (myCar2.speed, Car.count))
