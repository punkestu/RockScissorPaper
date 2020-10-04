import random
from os import system

option = 0
while option == 0:
	system("clear")#change "clear" into "cls" if you using windows
	print("welcome to rock scissor paper program")
	print("1. pvp")
	print("2. vs com")
	option = int(input("which mode you want to play?"))
	if option != 1 and option !=2:
		option = 0

system("clear")#change "clear" into "cls" if you using windows
if option == 1:
	p1 = str(input("r/s/p:?"))


i=0
for i in range(10):
	val = random.randint(1,9)

print(val)