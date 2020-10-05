import random
import time
from os import system

while True:
	option = 0
	while option == 0:
		system("clear")#change "clear" into "cls" if you using windows
		print("welcome to rock scissor paper program")
		print("1. pvp")
		print("2. vs com")
		print("[x]. exit")
		option = input("which mode you want to play?")#for choosing mode
		if option != "1" and option != "2" and option != "x":
			option = 0

	if option == "x":
		break;
	system("clear")#change "clear" into "cls" if you using windows
	p1 = str(input("player 1 >> r/s/p: "))#input for rock scissor and paper
	system("clear")
	if option == "1":#pvp
		p2 = str(input("player 2 >> r/s/p: "))
	if option == "2":
		i=0
		for i in range(100):
			val = random.randint(1,9)#random for com decicion
		if val%3 == 0:#com choose rock
			p2 = "r"
		if val%3 == 1:#com choose scissor
			p2 = "s"
		if val%3 == 2:#com choose paper
			p2 = "p"

		print("com >> r/s/p: ",p2)
		time.sleep(1)#delay

	system("clear")
	print(p1,"vs",p2)
	#duel!!!
	if p1 == p2:
		status = "draw"
	elif p1 == "r":
		if p2 == "s":
			status = "player 1 win"
		if p2 == "p":
			if option == "1":
				status = "player 2 win"
			else:
				status = "com win"
	elif p1 == "s":
		if p2 == "p":
			status = "player 1 win"
		if p2 == "r":
			if option == "1":
				status = "player 2 win"
			else:
				status = "com win"
	elif p1 == "p":
		if p2 == "r":
			status = "player 1 win"
		if p2 == "s":
			if option == "1":
				status = "player 2 win"
			else:
				status = "com win"

	print(status)
	option = str(input("do you want to play again?[y/n]: "))#continue or not?
	if option != "y" or option != "Y":
		break;

system("clear")
