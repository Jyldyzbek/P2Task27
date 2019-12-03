a = int(input('Vedite chislo-1: '))
b = int(input('Vedite chislo-2: '))

Chetnyi = []
Ne_chetnyi = []

for f in range (a, b+1):
    if f % 2 == 0:
        Chetnyi.append(f)
    else:
        Ne_chetnyi.append(f)

print(Chetnyi)
print(Ne_chetnyi)