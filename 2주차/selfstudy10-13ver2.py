##한 화면에 사진이 두개 출력되도록 수정하기##

from tkinter import *
from time import *

## 전역  변수 선언 부분 ## 
fnameList = ["jeju1.gif", "jeju2.gif", "jeju3.gif", "jeju4.gif", "jeju5.gif", "jeju6.gif", "jeju7.gif", "jeju8.gif", "jeju9.gif"]
photoList = [None] * 9
num = 0

## 함수 선언 부분 ## 
def clickNext() :
    global num  
    num += 1
    if num >= 8 :
        num = 0
    photo1 = PhotoImage(file = "gif/" + fnameList[num])
    pLabel1.configure(image = photo1)
    photo2 = PhotoImage(file = "gif/" + fnameList[num+1])
    pLabel2.configure(image = photo2)
    
    textCur1.configure(text=fnameList[num])
    textCur2.configure(text=fnameList[num+1])

    pLabel1.image = photo1
    pLabel2.image = photo2

    
def clickPrev() :
    global num
    num -= 1
    if num <= 0 :
        num = 8
    photo1 = PhotoImage(file = "gif/" + fnameList[num-1])
    pLabel1.configure(image = photo1)
    photo2 = PhotoImage(file = "gif/" + fnameList[num])
    pLabel2.configure(image = photo2)
    
    textCur1.configure(text=fnameList[num])
    
    pLabel1.image = photo1
    pLabel2.image = photo2
    
## 메인 코드 부분
window = Tk()
window.geometry("1400x500")
window.title("사진 앨범 보기")

btnPrev = Button(window, text = "<< 이전", command = clickPrev)
btnNext = Button(window, text = "다음 >>", command = clickNext)

textCur1 = Label(window,text=fnameList[0])
textCur2 = Label(window,text=fnameList[1])

photo1 = PhotoImage(file = "gif/" + fnameList[0])
photo2 = PhotoImage(file = "gif/" + fnameList[1])

pLabel1 = Label(window, image = photo1)  
pLabel2 = Label(window, image = photo2)  

btnPrev.place(x = 250, y = 10)
btnNext.place(x = 500, y = 10)

textCur1.place(x=325, y=10)
textCur2.place(x=380, y=10)

pLabel1.place(x = 15, y = 50)
pLabel2.place(x = 700, y = 50)
window.mainloop()
