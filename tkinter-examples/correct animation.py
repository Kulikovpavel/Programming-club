from tkinter import *
from math import *


root=Tk()
c = Canvas(root, width=1000, height=1000)
c.pack()

oval = c.create_oval(500, 500, 550, 550, fill='yellow')

def way():  # generator function for way, just sinus function
	n = 0
	while 1:
		n += pi/180
		dx = cos(n)
		dy = sin(n)
		
		yield dx, dy
		
gen = way()  # create new generator

def tick():
	dx, dy = next(gen)  # take next element in generator
	
	c.move(oval, dx, dy)  
	c.update()
	c.after(33, tick)

tick()

root.mainloop()
