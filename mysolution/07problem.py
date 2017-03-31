""" Statement:
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?"""

import math

def generate_prime(n):
    """
    n: nombre de nombre premier à trouver
    """

    # Initialisation de la liste prime et nombre à tester
    primes = [2]
    i = 3

    while len(primes) < n:
        is_prime = True

        # pour réduire le temps de calcul, on arrete la boucle à la moitié du nombre à tester
        sqrt_i = math.sqrt(i)
        for p in primes:
            if p > sqrt_i:
                break
            if i%p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
        i += 2
    return primes


print(generate_prime(10001))
