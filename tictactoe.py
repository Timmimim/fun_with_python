import sys

the_board = {'top_L': ' ', 'top_M': ' ', 'top_R': ' ',
			 'mid_L': ' ', 'mid_M': ' ', 'mid_R': ' ',
			 'low_L': ' ', 'low_M': ' ', 'low_R': ' ' }

def print_board (board):
	print(board['top_L'] + '|' + board['top_M'] + '|' + board['top_R'])
	print('-+-+-')
	print(board['mid_L'] + '|' + board['mid_M'] + '|' + board['mid_R'])	
	print('-+-+-')
	print(board['low_L'] + '|' + board['low_M'] + '|' + board['low_R'])

turn = 'X'
print("Enter target space as top_*/mid_*/low_*, replacing * with R/M/L.")
print("E.g.: mid_R is middle-right field, top_L is upper-left, ...\n")

for i in range(9):  # game ends after max 9 turns, no more fields
	print_board(the_board)
	print(f"\nTurn for {turn}. Move on which space?")
	
	move = input()

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

	the_board[move] = turn

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

	if turn == 'X':
		turn = 'O'
	else: turn = 'X'

# loop ended without winner
print_board(the_board)
print("\nGame ended in draw.")
