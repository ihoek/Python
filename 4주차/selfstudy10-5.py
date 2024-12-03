from tkinter import *
from tkinter.filedialog import *

## 함수 선언 부분 ##
def func_open() :
    filename = askopenfilename(parent=window,filetypes=(("GIF 파일",".gif"),("모든 파일","*.*")))
    photo = PhotoImage(file=filename)

    #1.width()과 height()값 찾기
    width = photo.width()
    height = photo.height()
    #2.for문을 통해 각 위치에 해당하는 좌표값에 색상을 찾기
    for i in range(0,height) :
        for j in range(0,width) :
            color = photo.get(j,i)
            #3.회색값으로 변경
            grey_color = int((color[0]+color[1]+color[2])/3)
            #4.이미지 픽셀값 변경
            photo.put("#%02x%02x%02x" % (grey_color,grey_color,grey_color),(j,i))
    
    pLabel.configure(image = photo)
    pLabel.image = photo

def func_exit() :
    window.quit()
    window.destroy

## 메인 코드 부분 ##
window = Tk()
window.geometry("400x400")
window.title("명화 감상하기")

photo = PhotoImage()
pLabel = Label(window, image=photo)
pLabel.pack(expand=1,anchor=CENTER)


mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label= "파일 열기",command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label= "프로그램 종료",command=func_exit)

window.mainloop()