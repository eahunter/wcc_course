import random

def play():

	print('Welcome to Welcome to Rock, Paper, Scissors!')
	
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

# Test this function
print 'You picked: ' + get_player_move()
	

	def check_move (move):
		if move == 'rock':
			return True
		elif move == 'paper':
			return True
		elif move == 'scissors':
			return True
		else :
			return False
		
	def get_computer_move():
		moves = ['rock', 'paper', 'scissors'];
		return random.choice(moves)

	print('The computer picked: ' + get_computer_move())
	
	def judge(move, moveB):

		if move == 'rock' and moves == 'paper':
			return "you lost"
		elif move == 'rock' and moves == 'scissors':
			return 'you won'
		elif move == 'paper' and moves == 'rock':
			return 'you won'
		elif move == 'paper' and moves == 'scissors':
			return 'you lost'
		elif move == 'scissors' and moves == 'rock':
			return 'you lost'
		elif move == 'scissors' and moves == 'paper':
			return 'you won'
play()
