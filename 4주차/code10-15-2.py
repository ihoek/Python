## 마우스 움직일때마다 레이블에 있는 위치값 변화주기 ##
## 마우스 커서가 위젯 위로 올라왔을 떄 <Enter>##
from tkinter import *

##함수 선언 부분##
def clickMouse(event) :
    print("x좌표:" + str(event.x)+", y좌표:" + str(event.y))
    txt=""
    txt += "마우스 커서가 (" + str(event.y) + "," + str(event.x) + ")에 위치해 있다"
    label1.configure(text=txt)

## 메인 코드 부분 ##
window = Tk()
window.geometry("600x600")

label1 = Label(window, text="이곳이 바뀜")

window.bind("<B1-Motion>",clickMouse)

label1.pack(expand=1, anchor=CENTER)
window.mainloop()