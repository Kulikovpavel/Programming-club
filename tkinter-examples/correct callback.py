from tkinter import *


def test():
    root = Tk()

    def callback(i):
        print(i)

    for i in range(9):
        btn = Button(root, text=i, command=lambda i=i: callback(i)).pack()
        print(btn)

    root.mainloop()

test()
