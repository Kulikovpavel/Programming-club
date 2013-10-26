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

points = [100, 140, 110, 110, 140, 100, 110, 90, 100, 60, 90, 90, 60, 100, 90, 110]
points = [[i, 500+ math.sin(i/30)*20]for i in range(0,100000) if i%120 == 0]+[10000,1000]+[0,1000]
w.create_polygon(points, outline=python_green, 
            fill='yellow', width=3)

mainloop()
