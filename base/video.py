from colorama import init, Fore, Back, Style
import random
from random import randrange
import time
init()
def clear():
	print("\033[2J\033[H", end="")
def colour(c):
	print(c +" ", end="")
while True:
	clear()
	colours = str("RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN").split(", ")
	coloursn = [1,2,3,4,5,6,7,8]
	#screen = [str("12345678" * 10),str("87654321" * 10)] * 10
	screen = []
	for e in str("e" * 25):
		line = ""
		for i in str("e" * 50):
			length = len(coloursn) - 1
			toadd = coloursn[randrange(0, length)]
			line += str(toadd)
		screen.append(line)
	for line in screen:
		for colourv in line:
			if int(colourv) == 1:
				colour(Back.RED)
			elif int(colourv) == 2:
				colour(Back.GREEN)
			elif int(colourv) == 3:
				colour(Back.YELLOW)
			elif int(colourv) == 4:
				colour(Back.BLUE)
			elif int(colourv) == 5:
				colour(Back.MAGENTA)
			elif int(colourv) == 6:
				colour(Back.CYAN)
			elif int(colourv) == 7:
				colour(Back.BLACK)
			elif int(colourv) == 8:
				colour(Back.WHITE)
			else:
				colour("u")
		print(Style.RESET_ALL)
	time.sleep(0.1)
#
