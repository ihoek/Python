## 클래스 선언 부분 ##
class Car : 
    color = ""
    speed = 0

    def __init__(self, name, speed) :
        self.name = name
        self.speed = speed

    def getName(self) :
        return self.name

    def getSpeed(self) :
        return self.speed

## 변수 선언 부분 ##
car1, car2 = None, None

## 메인 코드 부분 ##
myCar1 = Car("아우디",0)
myCar2 = Car("벤츠",30)

print("자동차1의 색상은 %s이며, 현재 속도는 %dkm입니다." % (myCar1.getName(), myCar1.getSpeed()))
print("자동차2의 색상은 %s이며, 현재 속도는 %dkm입니다." % (myCar2.getName(), myCar2.getSpeed()))
