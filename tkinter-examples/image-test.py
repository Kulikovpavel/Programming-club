from tkinter import *

w = Canvas(Tk(),width=1000, height=1000)

w.pack()

w.configure(background='yellow')
photo_image = PhotoImage(file="image.gif")
image = w.create_image(0,0, image=photo_image)
print(image)
text = w.create_text(0, 50, text='hello', font=('Times', '24', 'bold italic'))

def loop():
	w.move(image, 1, 1)
	w.move(text, 1, 1)
	w.after(35,loop)
	
w.after(30, loop)
mainloop()
