# Project Euler - Problem 20 - Factorial digit sum
# Find the sum of the digits in the number 100!

# take the factorial of 100, and prints out the sum of digits

def factorial(n):
   if n < 1:   # base case
       return 1
   else:
       returnNumber = n*factorial(n-1)  # recursive call
   return returnNumber

def sum_digits(n):
    s = 0
    while n:
        s += n%10
        n /= 10
    return s

print(sum_digits(factorial(100)))