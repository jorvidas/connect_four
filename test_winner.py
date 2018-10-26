game = "__________________________________________"

height = 6
width = 7

scenarios = []
scenarios.extend([game,
				 "xoooxxxx__________________________________",
				 "oooo___xxxx_______________________________",
				 "x______x______x______x____________________",
				 "x_______x_______x_______x_________________"]
)

def get_value(board, column, row, dims):
	width = dims[0]
	return board[column+row*width]

def check_row(board, player, to_win, dims):
	width, height = dims

	for row in range(height):
		for start_col in range(width-to_win+1):
			selection = board[row*width+start_col:row*width+start_col+to_win]
			print(selection)
			for idx in range(to_win):
				if selection[idx] != player:
					break
			else:
				return True

# Changes it from going across a row then moving to the next row to going up a
# column then moving to next column
def extract_columns(board, player, to_win):
	return "".join(["".join([board[x+i] for x in range(0,width*height, width)]) for i in range(width)])

def check_upwards(board, player, to_win, dims):
	width, height = dims

	for column in range(width-to_win+1):
		for row in range(height+1-to_win):
			to_check = []
			for i in range(to_win):
				to_check.append(get_value(board, column+i, row+i, dims))

# Checks a board for a winner
def check_winner(board, player, to_win):
	#check rows
	if check_row(board, player, to_win, (width, height)):
		return True

	#check columns
	columns = extract_columns(board, player, to_win)

	# can use same check as rows now that we have changed to column view
	if check_row(columns, player, to_win, (height,width)):
		return True

	#check upwards diagonal



for scenario in scenarios:
	print(scenario)
	print(check_winner(scenario, 'x', 4))