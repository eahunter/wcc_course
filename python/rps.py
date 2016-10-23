import random


	
	
def check_move (move):
	if move == 'rock':
		return True
	elif move == 'paper':
		return True
	elif move == 'scissors':
		return True
	else:
		return False
	
def get_player_move():
	move = raw_input('Pick your move: rock, paper, or scissors? ')
	while check_move(move) == False:
		print('Invalid move; pick again.')
		move = get_player_move()

		
	return move


def get_computer_move():
	moves = ['rock', 'paper', 'scissors'];
	return random.choice(moves)
		
		
def judge(move, moves):
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

def play():

	player = get_player_move()
	check_move(get_player_move)
	
	computer = get_computer_move()
	print('The computer picked: ' + computer)

	if player == computer:
		print('Tie!')
	elif(judge(player, computer) == True):
		print('You won!')
	else:
		print('The computer won!')
	
	play_again = raw_input('Play again? Type `y` or `n`: ')

	if(play_again == 'y'):
		play()
	else:
		print('Thanks for playing!')

# Run the game
play()