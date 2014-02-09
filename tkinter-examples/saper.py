from tkinter import *
import random


master = Tk()


def callback(i, j):
    print("click! i = %s, j = %s" % (i,j))
    b = button_list[i*m + j]
    button_state = state[i][j]

    if button_state == -1: 
    	text = "B"
    	color = "#FF0000"
    elif button_state == 0:
    	text = ""
    	color = "#F0F000"
    else:
    	text = str(button_state)
    	color = "#ffffe0"


    b.config(relief=SUNKEN, state=DISABLED, text=text, background=color)
    if state[i][j] == -1:
    	print("BOMB!!!@@@!@!")
    	game_over()

def game_over():
	pass

n = 30  # width
m = 30  # height
s = 100  # number of bombs

state = []  # array of n*m elements
for i in range(m):
	state.append([0]*n)


counter = 0

while counter < s:  # bomb creation
	x1 = random.randint(0, m-1)
	x2 = random.randint(0, n-1)
	if state[x1][x2] != -1:
		state[x1][x2] = -1
		counter += 1

button_list = []
for i in range(m):  # buttons create
	for j in range(n):
		b = Button(master, text="", width=3, command=lambda arg1=i, arg2=j : callback(arg1, arg2))
		b.grid(row=i, column=j)
		button_list.append(b)

def bomb_count(i, j):
	delta = [-1, 0, 1]
	counter = 0
	for elem in delta:
		for elem2 in delta:
			new_i = i + elem
			new_j = j + elem2
			if check_bounds(new_i, new_j):
				if state[new_i][new_j] == -1:
					counter += 1
	return counter

def check_bounds(i, j):
	return (0 <= i < m) and (0 <= j < n)

for i in range(m):  # count bombs in square
	for j in range(n):
		if state[i][j] != -1:
			state[i][j] = bomb_count(i, j)
	

mainloop()