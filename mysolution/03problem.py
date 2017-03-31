# statement:
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math


def divisors(n):
    """
    n: nombre à tester pour chercher ses diviseurs
    """

    factors = []

    #on utilise sqrt pour réduire le temps de calcul
    for i in range(2, math.floor(math.sqrt(n))+1):
        if n%i == 0:
            factors.append(i)
            factors.append(int(n/i))
    return factors

def is_prime(x):
    """
    x: nombre à tester s'il est nombre premier
    """
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

def largest_prime_factor(n):
    """
    n: nombre à partir duquel on cherche le nombre premier le plus grand
    """
    dlist = divisors(n)
    dlist.sort()
    dlist.reverse()

    for d in dlist:
        if is_prime(d):
            return d

print(largest_prime_factor(600851475143))
