### calculer les sommes d'un chiffre
# def somme_chiffre(n):
#     chiffrestr = str(n)
#     total = 0
#     for i in chiffrestr:
#         chiffreent = int(i)
#         total = total + chiffreent
#     return total
# print somme_chiffre(555)

def factorielle(x):
    chiffrestr = str(x)
    total = 0
    for i in chiffrestr:
        chiffreent = int(i)
        total = total * chiffreent
    return total

print factorielle(4)
