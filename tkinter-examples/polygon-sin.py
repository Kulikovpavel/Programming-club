from tkinter import *
import math
canvas_width = 1000
canvas_height =1000
python_green = "#476042"

master = Tk()

w = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
w.pack()

points = [[i, 500+ math.sin(i/30)*20]for i in range(0,2000) if i%2 == 0]+[10000,1000]+[0,1000]
w.create_polygon(points, outline=python_green, 
            fill='yellow', width=3)

mainloop()
