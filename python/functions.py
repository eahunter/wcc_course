#def mystery(x, y, z):
	#result = x , z * y
	#return result

# Test this function:
#print mystery('Hello', 3, '!') # Expected: 'Hello!!!'
#print mystery('Goodbye', 2, '@') # Expected: 'Goodbye@@'

def calculate_tip(meal_price, rating):
	if rating == 'A':
		tip = float(.20);
	elif rating == 'B':
		tip = float(.18);
	elif rating == 'C':
		tip = float(.15);
		
	return meal_price * tip
	
	
print(calculate_tip(30.50, 'C'))
print(calculate_tip(15.00, 'B')) 
print(calculate_tip(20.00, 'A'))