import math

ttoottaall = 0
for i in range(3, 999999): # highly doubt any number exists like this over a million, will change later if wrong
    stri = list(str(i))
    total = 0
    for j in stri:
        total += math.factorial(int(j))
    if i == total:
        ttoottaall += i

print ttoottaall
