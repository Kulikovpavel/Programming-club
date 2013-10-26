from tkinter import *
import math
def hard_job():
    x = 1000
    while True:
        x = math.log(x) ** 2.8
        root.update()
        print(x)
root=Tk()
button = Button()
button.pack()
root.after(500, hard_job)
root.mainloop()
