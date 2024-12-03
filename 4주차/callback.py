import tkinter as tk
import time

count=0

def counter_label(flag) :
    print("counter: "+ str(flag))
    label.config(text=str(flag))

root = tk.Tk()
root.title("Count Seconds")
label = tk.Label(root,fg="dark green")
label.pack()

button1 = tk.Button(root,text='Start', width=25, command=lambda: counter_label(1))
button = tk.Button(root,text='Stop',width=25,command=lambda: counter_label(0))

button.pack()
button1.pack()

root.mainloop()