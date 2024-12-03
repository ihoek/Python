from tkinter import *

def newfile() : 
    txt.delete(1,END)

def openfile() : 
    f = open('memo.txt','r')
    data = f.read()
    txt.delete(1,END)
    txt.insert(1,END)
    f.close()

def savefile() :
    f= open('memo.txt','w')
    f.write(txt.get(1,END))
    f.close()

def quit() :
    root.quit()
    root.destroy()

root = Tk()
root.title("메모장")
txt = Text(root)

txt.pack()

menubar = Menu(root)
file = Menu(menubar, tearoff=0)
file.add_command(label="새 파일", command=newfile)
file.add_command(label="열기", command=openfile)
file.add_command(label="저장", command=savefile)

file.add_separator()

file.add_command(label="종료", command=quit)
menubar.add_cascade(label="파일",menu=file)

root.config(menu = menubar)
root.mainloop()