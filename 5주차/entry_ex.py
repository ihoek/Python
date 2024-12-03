# bg,fg 색상 변경하기
# 입력이 1이면 배경색 red 입력이 2이면 배경색 blue로 변경
from tkinter import *

def btClick() :
    text = et.get()
    lb['text'] = text

    if text == "1" :
        window.config(bg="red")
    elif text == "2" :
        #lb.config(bg="blue")
        window.config(bg="blue")

    et.delete(0,END)


window = Tk()
window.geometry("400x400")

lb = Label(window, text="텍스트 입력", width=20)
et=Entry(window, width=20)
bt=Button(window, text="확인", width=20, bg="gray", command=btClick)

lb.pack()
et.pack()
bt.pack()

window.mainloop()