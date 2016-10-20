#name = raw_input('What is your name? ')
#print("Hi " + name)

#age = raw_input('How old are you?')
#dog_years = int(age) * 7
#print('You are ' + str(dog_years) + ' old in dog years.')

meal_cost = raw_input('How much was your meal?')
tip = float(meal_cost) * float(.20)
total = float(meal_cost) + tip
print('You should tip $' + str(round(tip, 2)))
print('Your total cost would be $' + str(total))
