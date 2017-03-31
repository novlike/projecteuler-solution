# Statement:
# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

#Initialisation de la somme, premier entier et deuxieme entier
total = 0
a = 1
b = 1

while True:
    d = a+b
    a = b
    b = d

    if b > 4000000:
        break

    if b%2 == 0:
        total = total + b

print(total)
