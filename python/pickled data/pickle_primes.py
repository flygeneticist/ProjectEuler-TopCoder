# quick script to pickle a list of all primes numbers
import pickle
import math

def nth_prime(n):
	"function will calculate the nth prime in a series."
    starting=3
    primes=[2]
    if n > 0:
        if starting%2 == 0:
            i = starting + 1
        else: 
            i = starting 
        while len(primes) < n:
            for e in primes:    
                prime_test = True # start loop assuming that the number is a prime.
                if e <= (math.sqrt(i)) and i%e == 0: # another number(e) divides evenly into i. 
                    prime_test = False # prime test has failed
                    break # break out of the loop
            if prime_test: # if i has passed all tests append it to the prime loop
                primes.append(i)
            i += 2
        return primes


primes_list = nth_prime(10001)
pickle.dump(primes_list, open('primes_list.pkl', 'wb'))