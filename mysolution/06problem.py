""" Statement:
The sum of the squares of the first ten natural numbers is,
1**2 + 2**2 + ... + 10**2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)* = 55*2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

# chercher la somme de puissance de 1-100
sum_square = 0
for i in range(1,101):
    sum_square += i**2

# chercher la puissance de la somme de 1-100
sqaure_sum = 0
sum_all = 0
for i in range(1,101):
    sum_all += i
    square_sum =  sum_all ** 2

print(square_sum - sum_square)

## une ligne
print(sum([x for x in range(101)])**2 - sum([x**2 for x in range(101)]))
