import random
import time

def displayIntro():
	print('''Вы находитесь в землях, заселенных драконами.
Перед собой вы видите две пещеры. В одной из них — дружелюбный дракон,
который готов поделиться с вами своими сокровищами. Во второй —
жадный и голодный дракон, который мигом вас съест.''')
	print()

def chooseCave():
	cave=''
	while cave !='1' and cave != '2':
		print('В какую пещеру вы пойдете? Нажмите клавишу 1 или 2')
		cave=input()


	return cave

def checkCave(chosenCave):
	print('Вы приближаетесь к пещере...')
	time.sleep(2)
	print('Ее темнота заставляет вас дрожать от страха...')
	time.sleep(3)
	print('Большой дракон выпрыгивает перед вами и...')	
	print()
	time.sleep(3)

	friendlyCave = random.randint(1,2)

	if chosenCave == str(friendlyCave):
		print('...делится с вами своими сокровищами')
	else:
		print('...моментально вас съедает')


playAgain = 'Да'
while playAgain == 'Да' or playAgain == 'д':
	displayIntro()
	caveNumber=chooseCave()
	checkCave(caveNumber)

	print('Попытать удачу еще раз? (да или нет)')
	playAgain = input()
