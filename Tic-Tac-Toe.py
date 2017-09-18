
#Printing welcome to Tic-Tac-Toe
#import sys

name = raw_input("Please enter your username: ")
print('\x1b[1;5;35m'+'WELCOME TO \nTIC-TAC-TOE\n'+name+'\x1b[0m')
	#print('\x1b[1;5;32m'+name+'\x1b[0m')
def print_menu():
	print("[S]tart game")
 	print("[T]ournament")
 	print("[Q]uit game")

#TODO: add options: Player vs Player, Player vs AI
def startGame():
	select_option_singlegame = raw_input("Do you want to play: \n1. Player vs Player \n2. Player vs AI \n3. Go back to menu\n").lower()
	
	if select_option_singlegame == "1":
		p1 = raw_input("Enter the name of player 1: ")
		p2 = raw_input("Enter the name of player 2: ")
		print("player1:" + p1  + "\n player2:" + p2)
	elif select_option_singlegame == "2":
		p1 = raw_input("Enter the name of the player")
		select_ai_difficulty = raw_input("What level of difficulty should the AI have? \n 1. Easy \n 2. Normal \n 3. Hard \n").lower()
		if select_ai_difficulty == "1":
			print("you have started a game vs ai easy " + p1)
		elif select_ai_difficulty == "2":
			print("ai Normal "+ p1)
		elif select_ai_difficulty == "2":
			print("ai hard "+ p1 )
	if select_option_singlegame == "3":
		pass
	else:
		print("You have not selected a vaild option ")
			

def startTournament():
	print("Tournament started")


loop = True

while loop:
	print_menu()
	select_option = raw_input("What do you want to do " + name +"?: ").lower()
	
	if select_option == "s":
		#here call the platfrom 
		startGame() 
	elif select_option == "t":
		#call 
		startTournament()

	elif select_option == "q":
			select_option_quit = raw_input("Do you really want to quit \n[y]/[n] \n").lower()
			if select_option_quit == "y":
				loop = False
			elif select_option_quit == "n":
				print("")
				
			

	else:
		print("You have not selected a vaild option "+ name)




