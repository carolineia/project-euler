import math

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def isPrimeNumber(n):
    for x in range(2, math.floor(math.sqrt(n)) + 1, 1): #could increment by 2 and only check odd numbers
        if (n % x == 0):
            return False
    return True

#input = 35 #600851475143

def largestPrimeFactor(number):
    half = math.ceil(number/2)
    if (half % 2 == 0):
        half += 1
    for i in range(half, 2, -2): # increment down from the square root
        #print(i)
        if (number % i == 0):
            if (isPrimeNumber(i)):
                return i
    return "no prime factors"

print(largestPrimeFactor(600851475143))