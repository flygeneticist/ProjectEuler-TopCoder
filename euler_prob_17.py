# Project Euler - Problem 17 - Number letter counts
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
# contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
# The use of "and" when writing out numbers is in compliance with British usage.

num_dict = {1:"one", 2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",
            11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",
            20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety"}

def thousands(place_holder):
    return num_dict[place_holder] + "thousand"


def hundreds(place_holder):
    return num_dict[place_holder] + "hundred"


def tens_and_ones(place_holder):
    if place_holder in num_dict:
        return num_dict[place_holder]
    else:
        tens_place = num_dict[int(str(place_holder)[0]+"0")]
        ones_place = num_dict[int(str(place_holder)[1])]
        return tens_place + ones_place


def print_a_number(number):
    s_number = str(number)
    long_version = ""
    places = len(s_number)
    # count if "and" is needed before tens place number
    counter = 0 # track multiple paths through the while loop

    while places != 0:
        counter += 1
        # if the place holder digit is 0 move on to the next
        if s_number[0] != "0":
            if places == 4: 
                long_version += thousands(int(s_number[0]))
            elif places == 3:
                # hundreths place needed
                long_version += hundreds(int(s_number[0]))
            elif places == 2:
                if counter > 1:
                    # append the "and" to be grammatically correct
                    long_version += "and"
                long_version += tens_and_ones(int(s_number[0:]))
                break
            elif places == 1:
                if counter > 1:
                    # append the "and" to be grammatically correct
                    long_version += "and"
                long_version += num_dict[int(s_number)]

        # truncate the string by one
        s_number = s_number[1:] 
        # take new reading on number of places left to check
        places = len(s_number)

    return long_version


def collect_numbers(limit):
    all_nums = []
    for e in range(1,limit+1):
        all_nums.append(print_a_number(e))
    return all_nums

def clean_up_count(limit):
    num_list = collect_numbers(1000)
    clean_list = "".join(num_list)
    return len(clean_list)

print(clean_up_count(1000))
#print(collect_numbers(125))