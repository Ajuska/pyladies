# nejmensi_cislo = int(input('Napiš číslo:'))
#
# for c in range (4):
#     cislo = int(input('Napiš číslo:'))
#     if cislo < nejmensi_cislo:
#         nejmensi_cislo = cislo
#
# print(nejmensi_cislo)


# for c in range (5):
#     cislo = int(input('Napiš číslo:'))
#     if c == 0:
#         nejmensi_cislo = cislo
#     else:
#         if cislo < nejmensi_cislo:
#             nejmensi_cislo = cislo
#
# print(nejmensi_cislo)

l = list()
for v in range(5):
    l.append(int(input()))
lsorted = sorted(l)
print(lsorted[0])
