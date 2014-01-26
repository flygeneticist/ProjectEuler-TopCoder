#  Project Euler - Problem 21 - Amicable numbers
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# Evaluate the sum of all the amicable numbers under 10000.

import math

# uses the square root of n to reduce search further and appends pairs of factors
def sum_of_factors(n): 
    factors = []
    for i in range(1,int(math.ceil(math.sqrt(n)))):
        if n%i == 0:
            factors.append(i)
            factors.append(n//i)
    factors.sort()
    return (n, sum(factors[0:-1])) # returns tuple with n and the sum less n

# setup the list of all numbers and their resulting sum of factors
def setup_factors_list(limit):
    factors_list = []
    for n in range(1,limit):
        factors_list.append(sum_of_factors(n))
    return factors_list

# evaluate the numbers and factor sums to find amicable numbers and return a sum of amicable numbers subset
def eval_amicable_numbers(factors_list):
    amicable_nums = []
    for a,sum_a in factors_list:
        for b,sum_b in factors_list:
            if a != b:
                if sum_a == b and sum_b == a:
                    amicable_nums.append(a)
                    amicable_nums.append(b)
    return sum(set(amicable_nums))

# runtime code
print(eval_amicable_numbers(setup_factors_list(10000)))