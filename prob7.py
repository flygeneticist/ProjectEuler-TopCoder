# Project Euler - Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

primes = [2,3,5,7,11,13] # seed the list of primes with 2 to avoid checking obvious nums
i = 15
while len(primes) < 10001:
    if (i%3 == 1) and (i%5 == 1) and (i%7 == 1) and (i%11 == 1) and (i%13 == 1):
        primes.append(i)
    i += 2
print(primes)
