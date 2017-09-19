
#Printing welcome to Tic-Tac-Toe
#import sys
#class Menu:

name = raw_input("Please enter your username: ")
print('\x1b[1;5;35m'+'WELCOME TO \nTIC-TAC-TOE\n'+name+'\x1b[0m')
	#print('\x1b[1;5;32m'+name+'\x1b[0m')

#prints the menu with its options
def print_menu():
	print("[S]tart game")
 	print("[T]ournament")
 	print("[Q]uit game")


def is_AI():
	select_ai_difficulty = raw_input("What level of difficulty should the AI have? \n 1. Easy \n 2. Normal \n 3. Hard \n").lower()

	if select_ai_difficulty == "1":
		#print(select_ai_difficulty + " easy")
		return select_ai_difficulty
		#start game and call the platform
	elif select_ai_difficulty == "2":
		#print(select_ai_difficulty+ " normal")
		return select_ai_difficulty
		#start game and call the platform
	elif select_ai_difficulty == "3":
		#print(select_ai_difficulty+ " hard")
		return select_ai_difficulty
		#start game and call the platform
	else:
		print("You have not selected a vaild option ")
		


#TODO: add call to the platform and send information about the user such as name. 
#function for starting the game and printing the options for the game
def startGame():
	#prints the options for the user and takes an input 1-3
	select_option_singlegame = raw_input("Do you want to play: \n1. Player vs Player \n2. Player vs AI \n3. Go back to menu\n").lower()
	#Player vs Player
	if select_option_singlegame == "1":
		# add the player name for player 1
		player1 = raw_input("Enter the name of player 1: ")
		# add the player name for player 2
		player2 = raw_input("Enter the name of player 2: ")
		#not needed in later versions
		print("player1:" + p1  + "\n player2:" + p2)
		#now start the game and call the platform 
		#send information about player names to platform
	
	#Player vs AI
	elif select_option_singlegame == "2":
		# add the player name send this to the platform
		player = raw_input("Enter the name of the player: ")
		
		#get the difficulty for the AI (int)
		ai_level = is_AI()
		print(ai_level)
		#send difficulty to platfrom 

		

	

def startTournament():
	print("Tournament started")
	#create a list 
	tournament_players = raw_input("How many players will there be in the Tournament 2-8: ")
	#print(tournament_players)
	#create a for loop to fill list and ask user if AI or Player
	player_list = []
	#for tournament_players in player_list:


loop = True

while loop:
	print_menu()
	select_option = raw_input("What do you want to do " + name +"?: ").lower()
	
	if select_option == "s":
		startGame() 
	
	elif select_option == "t":
		startTournament()
	
	elif select_option == "q":
			select_option_quit = raw_input("Do you really want to quit \n[y]/[n] \n").lower()
			if select_option_quit == "y":
				loop = False
			elif select_option_quit == "n":
				print("")		

	else:
		print("You have not selected a vaild option "+ name)




