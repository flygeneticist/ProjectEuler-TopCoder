#  Project Euler - Problem 22 - Names scores
# Using names.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. 
# Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
# So, COLIN would obtain a score of 938 x 53 = 49714.

# What is the total of all the name scores in the file?
import re

with open('euler_prob_22_names.txt','r') as data:
    pattern = re.compile('"\s*,\s*"')
    for line in data:
        names = pattern.split(line)

# lazy correction of the edge exception cases from the regular expression(first and last names have a " included)
names[0] = names[0][1:]
names[-1] = names[-1][:-1]

# go through each name, sorted in alphabetial order, force lowercase, and then calcualte the score based on the ordinal result minus 96
# ie. 'a' = ord('a')-96) = (97-96) = 1
counter = 0
total_score = 0

for name in sorted(names):
    name_score = 0 # reset name score
    counter += 1 # increment counter to track overall position in list
    name = name.lower() # force lowercase for ord()
    # calculate the alph score for the chars in the name
    for char in name: 
        name_score += (ord(char)-96)
    # calculate the name score relative to the postion in the list(ie. the counter var)
    name_score = name_score * counter
    # add final name score to the total score for the list
    total_score += name_score

print(total_score)