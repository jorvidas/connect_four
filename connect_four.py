#connect four
#grid is 7 wide, 6 tall
#four in a row wins

width = 7
height = 6
to_win = 4

#inserts the players character into the game string
def replace_str_index(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])

#figures out where the piece will fall to if given the column dropped into
def get_loc_from_col(column, game):
	while True:
		for i in range(height):
			if game[column-1+i*width] != "_":
				return column-1+(i-1)*width
		return (height-1)*width+column-1


#this is the game board starting in the upper left corner
# ' ' is blank and 'x' 'o' are the players
game_board = '_' * 6 * 7

#game_board = replace_str_index(game_board, 35, 'x')
#game = "xxxxoooooxoxoxoxo________________xoxoxoxoxoxo"
#game[0] = o

#print board
def print_gameboard():
	for i in range(width):
		print(i+1, end=" ")
	print()
	for i in range(height):
		for j in range(width):
			print(game_board[i*width+j], end=" ")
		print()

#allow placing of piece
def get_move():
	column = int(input("Which column would you like to drop into? "))
	return column

#place piece into game
def update_board(game, choice, player):
	idx = get_loc_from_col(choice, game)
	return replace_str_index(game, index=idx, replacement=player)

#check to see if winner, i only want to check based on where the drop happened
def check_for_winner():
	#check row
	for i in range(to_win):
		if column - i > 0 and column + i - to_win - 1 <= width:
			return 

	#check vertical
	#check diagonals

#loop back

while True:
	print_gameboard()
	column = get_move()
	game_board = update_board(game_board, column, "x")
	print_gameboard()
	#check_winner()
	break