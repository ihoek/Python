# 메뉴에 선의 굵기를 선택하는 메뉴항목을 추가하시오. 굵기는 (1-3), check 메뉴 사용
from tkinter import *

## 함수 선언 부분 ##
def paint(event) :
    global penWidth
    x1, y1 = (event.x-1), (event.y-1)
    x2, y2 = (event.x+1), (event.y+1)
    canvas.create_oval(x1,y1,x2,y2, width=penWidth,fill="black")
    
def select1() :
    global penWidth
    penWidth = 1

def select2() :
    global penWidth
    penWidth = 2

def select3() :
    global penWidth
    penWidth = 3

## 메인 함수 부분 ##
window = Tk()
window.title("그림판")
canvas = Canvas(window)
canvas.pack()

canvas.bind("<B1-Motion>", paint)

menubar = Menu(window)
file = Menu(menubar, tearoff=0)

file.add_checkbutton(label="굵기 설정 : 1",command=select1)
file.add_checkbutton(label="굵기 설정 : 2",command=select2)
file.add_checkbutton(label="굵기 설정 : 3",command=select3)

menubar.add_cascade(label="파일",menu=file)

window.config(menu = menubar)

window.mainloop()