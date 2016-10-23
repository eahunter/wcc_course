import random




def check_move (move):
	if move == 'rock':
		return True
	elif move == 'paper':
		return True
	elif move == 'scissors':
		return True
	else :
		return False


# This function is provided; no edits are needed.
# Parameters: None
# Returns: String of 'rock', 'paper', or scissors'
# Prompts the user for a move
# Makes sure that move is valid; if it's not, continues to ask user for a move
def get_player_move():

    # Prompt the user to enter their move
    move = raw_input('Pick your move: rock, paper, or scissors? ')

    # This will happen on a loop until the user enters a valid move
    while check_move(move) == False:
        print('Invalid move; pick again.')
        # Run this function again, so they're asked to enter a new move
        move = get_player_move()

    # If they get out of the while loop, it means they
    # entered a valid move, so return it
    return move

# This function is provided; no edits are needed
# Parameters: None
# Returns: String of 'rock', 'paper', or 'scissors'
def get_computer_move():
    moves = ['rock', 'paper', 'scissors'];
    return random.choice(moves)

print get_computer_move() # Expected: 'rock', 'paper', or 'scissors'
print get_computer_move() # Expected: 'rock', 'paper', or 'scissors'
print get_computer_move() # Expected: 'rock', 'paper', or 'scissors'
	
