from tkinter import *

window = Tk()
menubar = Menu(window)
window.config(menu=menubar)

menu_1 = Menu(menubar,tearoff=0)
menu_1.add_command(label="&하위메뉴 1-1")
menu_1.add_command(label="하위 메뉴 1-2")
menu_1.add_separator()
menu_1.add_command(label="하위 메뉴 1-3",command=close)
menu_1.add_cascade(label = "상위 메뉴 1",menu=menu_1)

menu_2 = Menu(menubar,tearoff=0,selectcolor="red")
menu_2.add_radiobutton(label="하위메뉴 2-1",state="disable")
menu_2.add_radiobutton(label="하위 메뉴 2-2")
menu_2.add_radiobutton(label="하위 메뉴 2-3")
menu_2.add_cascade(label = "상위 메뉴 2",menu=menu_2)

menu_3 = Menu(menubar,tearoff=0)
menu_3.add_checkbutton(label="하위메뉴 3-1")
menu_3.add_checkbutton(label="하위 메뉴 3-2")
menu_2.add_cascade(label = "상위 메뉴 2",menu=menu_3)



window.mainloop()