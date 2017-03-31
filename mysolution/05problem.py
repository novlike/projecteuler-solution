"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

def forever(start=1):
    count = start
    while True:
        yield count
        count += 1

for n in forever():
    if n%11==0 and n%12==0 and n%13==0 and n%14==0 and n%15==0 and n%16==0 and n%17==0 and n%18==0 and n%19==0 and n%20==0 :
        break
print(n)

# better solution that I found:
#
# i = 1
# for k in (range(1, 21)):
#     if i % k > 0:
#         for j in range(1, 21):
#             if (i*j) % k == 0:
#                 i *= j
#                 break
# print i
#
