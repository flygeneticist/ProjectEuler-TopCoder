# Project Euler - Problem 16 - Power digit sum
# What is the sum of the digits of the number 2^1000?

total = 0
power_digit = str(2**1000)

for n in power_digit:
    total += int(n)
    
print(total)