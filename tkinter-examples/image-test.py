from tkinter import *
from math import *

def get_direction(x1, y1, x2, y2):
	deltax = x2 - x1
	deltay = y2 - y1
	theta = atan2(deltay, deltax)
	return cos(theta), sin(theta)

root = Tk()	
w = Canvas(root,width=1000, height=1000)
w.pack()

w.configure(background='yellow')
photo_image = PhotoImage(file="image.gif")
image = w.create_image(0,0, image=photo_image)
text = w.create_text(0, 50, text='hello', font=('Times', '24', 'bold italic'))

def loop():
	x,y = w.winfo_pointerxy()
	xr = w.winfo_rootx()
	yr = w.winfo_rooty()
	x = x - xr
	y = y - yr

	xi, yi = w.coords(image)  # get image coordinate
	dx, dy = get_direction(xi, yi, x, y)
		
	w.move(image, dx, dy)
	w.move(text, 1, 1)
	w.after(35,loop)
	
w.after(30, loop)

mainloop()
