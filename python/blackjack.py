import random

#                                        J   Q   K   A
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

random.shuffle(cards)

print(cards) # To see the list after being shuffled

# Round 1
player_card1 = cards.pop()
computer_card1 = cards.pop()

print('Player card: ' + str(player_card1))
print('Computer card:  ' + str(computer_card1))

print(cards) # To see the list after two cards have been popped off.

decision = raw_input('\nIf you want to stay type `s`, if you want to hit type `h`: ')

if decision == 'h':
	player_card2 = cards.pop();
	print('Player card:  ' + str(player_card1) + ', ' + str(player_card2));
	computer_card2 = cards.pop();
	print('Computer card:  ' + str(computer_card1) + ', ' + str(computer_card2));
elif decision == 's':
	computer_card2 = cards.pop();
	print('Player card: ' + str(player_card1));
	print('Computer card:  ' + str(computer_card1) + ', ' + str(computer_card2));

decision = raw_input('\nIf you want to stay type `s`, if you want to hit type `h`: ')

computer_total = computer_card1 + computer_card2


if decision == 'h':
	player_card3 = cards.pop();
	print('Player card:  ' + str(player_card1) + ', ' + str(player_card2) + ', ' + str(player_card3));
	
	if int(computer_total) < int(16):
		computer_card3 = cards.pop();
		print('Computer card:  ' + str(computer_card1) + ', ' + str(computer_card2) + ', ' + str(computer_card3));
	elif int(computer_total) > int(16):
		computer_card3 = 0
		print('Computer card:  ' + str(computer_card1) + ', ' + str(computer_card2));
		
elif decision == 's':
	print('Player card:  ' + str(player_card1) + ', ' + str(player_card2));
	player_card3 = 0
	if int(computer_total) < int(16):
		computer_card3 = cards.pop();
		print('Computer card:  ' + str(computer_card1) + ', ' + str(computer_card2) + ', ' + str(computer_card3));
	elif int(computer_total) > int(16):
		computer_card3 = 0
		print('Computer card:  ' + str(computer_card1) + ', ' + str(computer_card2));

		
print(' ')
print(' ')		
print('Game over...')

player_final = player_card1 + player_card2 + player_card3

computer_final = computer_card1 + computer_card2 + computer_card3




if int(player_final) <= int(21) and int(computer_final) > int(21):
	print('You win! (You were closest to 21.)')

elif int(computer_final) <= int(21) and int(player_final) > int(21):
	print('The computer wins! (It was closest to 21.)')
	
elif int(computer_final) == int(21) and int(player_final) == int(21):
	print('It is a tie!')

elif int(computer_final) > int(21) and int(player_final) > int(21):
	print('It is a tie!')