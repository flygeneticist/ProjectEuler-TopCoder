# Project Euler - Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

# Taken from "paul-scott.com" discussion on finding primes:
# 1) Iterate over the whole number system, ignoring even numbers greater than 2 (2, 3, 5, 7, ...)
# 2) For each integer, p, check if p is prime:
#       a) Iterate over the primes already found which are less than the square-root of p
#       b) For each prime in this set, f, check to see if it is a factor of p:
#               1) If f divides p then p is non-prime. Continue from 2 for the next p.
#       c) If no factors are found, p is prime. Continue to 3.
# 3) If p is not the nth prime we have found, add it to the list of primes. Continue from 2 for the next p.
# 4) Otherwise, p is the nth prime we have found and we should return it.

import math

def nth_prime(n, starting=3):
# function will calculate the nth prime in a series. 
    if n > 0:
        primes = [2] # seed the list of primes with 2 to avoid checking obvious nums
        if starting%2 == 0:
            i = starting + 1
        else:
            i = starting
        
        while len(primes) < n:
            for e in primes:    
                prime_test = True # start loop assuming that the number is a prime.
                if e <= (math.sqrt(i)):
                    if i%e == 0: # another number(e) divides evenly into i. 
                        prime_test = False # prime test has failed
                        break # break out of the while loop
            if prime_test: # if i has passed all tests append it to the prime loop
                primes.append(i)
            i += 2
        
        return primes


if __name__ == "__main__":
    print(nth_prime(1001)[1000])