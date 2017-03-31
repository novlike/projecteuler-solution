"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers."""

def is_palindrome(n):
    """
    n: nombre à tester s'il est palindromique
    """

    # pour savoir s'il est palindromique, le nombre doit être une chaine de caractère
    n = str(n)
    if n == n[::-1]: # [::-1] : reverse de la chaine de caractère
        return True
    return False

#initialisation pour comparer les chiffres palindromiques plus grand qu'au précédent 
m = 0
for i in range(1, 1000):
    for j in range(i,1000):
        p = i*j
        if is_palindrome(p):
            if p > m:
                m = p

print(m)
