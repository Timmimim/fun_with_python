# Author: Timm Kühnel
# Inspired by: Automate The Boring Stuff With Python - Al Sweigert

# Built with Python3.7 on KUbuntu 18.4, may or may not work on other systems

import sys		# a little overkill for closing programm on victory, but hey...

# init a tictactoe grid
the_board = {'top_L': ' ', 'top_M': ' ', 'top_R': ' ',
			 'mid_L': ' ', 'mid_M': ' ', 'mid_R': ' ',
			 'low_L': ' ', 'low_M': ' ', 'low_R': ' ' }

# helper to visualize board as terminal prints
def print_board (board):
	print(board['top_L'] + '|' + board['top_M'] + '|' + board['top_R'])
	print('-+-+-')
	print(board['mid_L'] + '|' + board['mid_M'] + '|' + board['mid_R'])	
	print('-+-+-')
	print(board['low_L'] + '|' + board['low_M'] + '|' + board['low_R'])

# marks symbol of current player, thus who's turn it is
# player 'X' always starts
turn = 'X'

print("Enter target space as top_*/mid_*/low_*, replacing * with R/M/L.")
print("E.g.: mid_R is middle-right field, top_L is upper-left, ...\n")

for i in range(9):  # game ends after max 9 turns, no more fields
	print_board(the_board)
	print(f"\nTurn for {turn}. Move on which space?")
	
	# wait for keayboard input of target space, i.e. next move
	move = input()

	# check validity of move:  valid key + field not yet occupied
	while (move not in the_board.keys()) or (not the_board[move] == ' '):
		if move not in the_board.keys():
			print("\nPlease try again.")
			print("Enter target space as top_*/mid_*/low_*, replacing * with R/M/L.")
			move = input()
		else:
			print("\nKey was entered correctly, but space was already taken.")
			print("Please try again.")
			move = input()
	print("")

	# update the target space in grid with current player's symbol
	the_board[move] = turn

	# check for a winner --> three in a row, column or diagonale
	if( 
		   ( the_board['top_L'] == the_board['top_M'] and the_board['top_M'] == the_board['top_R'] and not the_board['top_R'] == ' ' )
		or ( the_board['mid_L'] == the_board['mid_M'] and the_board['mid_M'] == the_board['mid_R'] and not the_board['mid_R'] == ' ' )
		or ( the_board['low_L'] == the_board['low_M'] and the_board['low_M'] == the_board['low_R'] and not the_board['low_R'] == ' ' )
		or ( the_board['top_L'] == the_board['mid_L'] and the_board['mid_L'] == the_board['low_L'] and not the_board['top_L'] == ' ' )
		or ( the_board['top_M'] == the_board['mid_M'] and the_board['mid_M'] == the_board['low_M'] and not the_board['top_M'] == ' ' )
		or ( the_board['top_R'] == the_board['mid_R'] and the_board['mid_R'] == the_board['low_R'] and not the_board['top_R'] == ' ' )
		or ( the_board['top_R'] == the_board['mid_M'] and the_board['mid_M'] == the_board['low_L'] and not the_board['top_R'] == ' ' )
		or ( the_board['top_L'] == the_board['mid_M'] and the_board['mid_M'] == the_board['low_R'] and not the_board['top_L'] == ' ' )
		):
		print_board(the_board)
		print(F"\nWinner:   {turn}\n")
		sys.exit()

	# if there was no winner, set next players turn before loop repeats
	if turn == 'X':
		turn = 'O'
	else: turn = 'X'

# loop ended without winner
print_board(the_board)
print("\nGame ended in draw.")

# TODO: make terminal logs pretty
# TODO: introduce ASCII art celebration animation, and 'Meh' for draw

""" Note: 
	This is a "one file does all" mini-game. 
	To not blow this out of proportion (yet), there is no modularization (yet).
	There will be, if this is to be expanded to a full UI-Game using Qt.
	So, we will see...
"""