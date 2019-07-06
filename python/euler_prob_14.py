# Project Euler - Problem 14 - Longest Collatz sequence
# Which starting number, under one million, produces the longest chain?
# Rules: 
# n => n/2 (n is even)
# n => 3n + 1 (n is odd)

def process(num):
    if num == 1: # terminating 1
        return 1 
    elif num%2 == 0: # for even numbers
        return num/2
    else: # for odd numbers
        return 3*num+1

def chain(n):
    chain = [n]
    while n != 1:
        n = process(n)
        chain.append(n)
    return chain

def longest_chain_finder(max):
    longest_chain = 0
    longest_e = 0
    for e in range(1,max+1):
        e_chain = len(chain(e))
        if e_chain > longest_chain:
            longest_chain = e_chain
            longest_e = e
    return (longest_e,longest_chain)

print longest_chain_finder(1000000)
