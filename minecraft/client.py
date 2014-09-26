import socket
from math import *
import time


def rainbow(sock, position=(0,0,0)):
	colors = [14, 1, 4, 5, 3, 11, 10]
	height = 90
	width = 128

	for x in range(0, width):
		for colourindex in range(0, len(colors)):
			y = floor(sin((x / width) * pi) * height + colourindex)
			color = colors[len(colors) - 1 - colourindex]
			command = "setblock {} {} {} {} {} destroy".format(x+position[0], y+position[1], position[2], "minecraft:wool", colors[len(colors) - 1 - colourindex])
			sock.send(command.encode())
			time.sleep(1/30)
	
	
if __name__ == "__main__":			
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print('connecting to server')
	sock.connect(('localhost', 9090))
	sock.settimeout(1)
	print('connected, sending request')

	while True:
		i = input()	
		if i == "quit":
		  sock.close()
			break
		elif i == "rainbow":
			rainbow(sock, (0, 95, 0))
		else:
			sock.send(i.encode())
