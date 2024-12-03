from tkinter import *

def btClick() :
    text = et.get()
    lb['text'] = text
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