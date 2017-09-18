
#Printing welcome to Tic-Tac-Toe
import sys

name = raw_input("Please enter your username: ")
print('\x1b[1;5;35m'+'WELCOME TO \nTIC-TAC-TOE\n'+name+'\x1b[0m')
	#print('\x1b[1;5;32m'+name+'\x1b[0m')
def print_menu():
	print("[S]tart game")
 	print("[T]ournament")
 	print("[Q]uit game")


loop = True

while loop:
	print_menu()
	select_option = raw_input("What do you want to do " + name +"?: ").lower()
	
	if select_option == "s":
		print("u have started a game")

	elif select_option == "t":
		print("Tournament started")

	elif select_option == "q":
			select_option_quit = raw_input("Do you really want to quit \n[y]/[n] \n").lower()
			if select_option_quit == "y":
				loop = False
			elif select_option_quit == "n":
				print("")
				
			

	else:
		print("You have not selected a vaild option "+ name)




