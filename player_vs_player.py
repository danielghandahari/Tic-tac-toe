#Handle the Tic-tac-toe player vs player
#Define the board
board = [" "," "," ",
		 " "," "," ",
		 " "," "," "]

def print_board():
	"""Function to print the board"""
	print("======= Your movement =======")
	print("           " + "-------")
	print("           " + "|" + board[0] + "|" + board[1] + "|" + board[2] + "|")
	print("           " + "-------")
	print("           " + "|" + board[3] + "|" + board[4] + "|" + board[5] + "|")
	print("           " + "-------")
	print("           " + "|" + board[6] + "|" + board[7] + "|" + board[8] + "|")
	print("           " + "-------")
	print("============================= \n")

def print_board_dummies():
	"""Function to print the board dummies, so the player know the position"""
	print("======= Board Dummies =======")
	print("           " + "-------")
	print("           " + "|" + "1" + "|" + "2" + "|" + "3" + "|")
	print("           " + "-------")
	print("           " + "|" + "4" + "|" + "5" + "|" + "6" + "|")
	print("           " + "-------")
	print("           " + "|" + "7" + "|" + "8" + "|" + "9" + "|")
	print("           " + "-------")
	print("============================= \n")


def player_1_move():
	"""Function to handle player X movement"""
	print_board()
	#Capture player 1 movement
	try:
		move = raw_input("Where do you want to move " + "p1" + "? ")
		move = int(move) - int(1)
		#Check if the player inputs valid input i.e 0-8
		if move > -1 and move < 9:
			#Check if the space is empty or not
			if board[move] == " ":
				board[move] = "X"
			else:
				print("The space is taken!")
				player_1_move()
		else:
			print("Please write valid input i.e 1-9!")
			player_1_move()
	#If user enter non-integer input
	except ValueError:
		print("Please write valid input i.e 1-9!")
		player_1_move()
	

def player_2_move():
	"""Function to handle player O movement"""
	print_board()
	#Capture player O movement
	try:
		move = raw_input("Where do you want to move " + "p2" + "? ")
		move = int(move) - int(1)
		#Check if the player inputs valid input i.e 0-8
		if move > -1 and move < 9:
			#Check if the space is empty or not
			if board[move] == " ":
				board[move] = "O"
			else:
				print("The space is taken")
				player_2_move()
		else:
			print("Please write valid input i.e 1-9!")
			player_2_move()
	#If user enter non-integer input
	except ValueError:
		print("Please write valid input i.e 1-9!")
		player_2_move()

while True:
	print_board_dummies()
	player_1_move()


	#Check if player win
	if (board[0] == "X" and board[1] == "X" and board[2] == "X") or \
		(board[3] == "X" and board[4] == "X" and board[5] == "X") or \
		(board[6] == "X" and board[7] == "X" and board[8] == "X") or \
		(board[0] == "X" and board[3] == "X" and board[6] == "X") or \
		(board[1] == "X" and board[4] == "X" and board[7] == "X") or \
		(board[2] == "X" and board[5] == "X" and board[8] == "X") or \
		(board[0] == "X" and board[4] == "X" and board[8] == "X") or \
		(board[2] == "X" and board[4] == "X" and board[6] == "X"):
		print("Congratulation!" + "p1" + "win!")
		print_board()
		break

	print_board_dummies()
	player_2_move()

	#Check if player win
	if (board[0] == "O" and board[1] == "O" and board[2] == "O") or \
		(board[3] == "O" and board[4] == "O" and board[5] == "O") or \
		(board[6] == "O" and board[7] == "O" and board[8] == "O") or \
		(board[0] == "O" and board[3] == "O" and board[6] == "O") or \
		(board[1] == "O" and board[4] == "O" and board[7] == "O") or \
		(board[2] == "O" and board[5] == "O" and board[8] == "O") or \
		(board[0] == "O" and board[4] == "O" and board[8] == "O") or \
		(board[2] == "O" and board[4] == "O" and board[6] == "O"):
		print("Congratulation!" + "p2" + "win!")
		print_board()
		break

	#Check if is Tie
	tie = True
	if " " in board:
		tie = False
	elif tie == True:
		print("Tie! No player wins!")
		print_board()
		break