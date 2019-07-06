# Project Euler - Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.


# Sieve of Eratosthenes
# 1. Make a list of all numbers from 3 to N skipping even numbers.
# 2. Find the next number p not yet crossed out. This is a prime.
#       a. If it is greater than N , go to 5.
# 3. Cross out all multiples of p which are not yet crossed out.
# 4. Go to 2.
# 5. The numbers not crossed out are the primes not exceeding N .

import numpy as np 


def find_all_primes_up_to(limit):
    is_prime = np.ones(limit + 1, dtype=np.bool)
    for n in xrange(2, int(limit**0.5 + 1.5)): 
        if is_prime[n]:
            is_prime[n*n::n] = 0
    return np.nonzero(is_prime)[0][2:]


if __name__ == "__main__":
    prime_limit = input("enter prime number limit: ")
    print(sum(find_all_primes_up_to(prime_limit)))