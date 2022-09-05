import random
import array

# PeopleSoft domain connect password. 
# Bettwen 8 and 20 characters in length.
# Ensure the password contains only alphanumeric characters.

MIN_LEN = 8
MAX_LEN = 20

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
					'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
					'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
					'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
					'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
					'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
					'Z']

COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS

def generate():
	# randomly select at least one character from each character set above
	rand_digit = random.choice(DIGITS)
	rand_upper = random.choice(UPCASE_CHARACTERS)
	rand_lower = random.choice(LOCASE_CHARACTERS)

	temp_pass = rand_digit + rand_upper + rand_lower

	# fill the rest by selecting randomly from the combined list
	for x in range(MAX_LEN - 4):
		temp_pass = temp_pass + random.choice(COMBINED_LIST)
		
		temp_pass_list = array.array('u', temp_pass)
		random.shuffle(temp_pass_list)

	password = ""
	for x in temp_pass_list:
			password = password + x
	
	return password