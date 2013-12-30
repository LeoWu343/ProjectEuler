tri = set()
pent = set()
hexa = []
for i in range(1, 100001):
    tri.add((i*(i+1))/2)
    pent.add((i*(3*i-1))/2)
    hexa.append(i*(2*i-1))
for i in hexa:
    if i in tri and i in pent:
        print i
