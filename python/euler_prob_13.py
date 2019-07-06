# Project Euler - Problem 13 - Large Sum
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

# the 100, 50 digit numbers given were stored as a plain text file. 
# for each line in the text file, representing one number, the string was convered to an integer.
# the integer was added to the running total for the file. 
# the final step converts the integer total back to a string form and prints out a slice of the first 10 digits.

with open('euler_prob_13_data.txt', 'r') as data:
	total = 0
	for line in data:
		total += int(line)

print(str(total)[0:10])
