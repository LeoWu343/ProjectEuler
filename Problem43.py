import itertools

counter = 0
for i in itertools.permutations("0123456789"):
    a = (float(i[1]+i[2]+i[3]) / 2.0) % 1.0
    b = (float(i[2]+i[3]+i[4]) / 3.0) % 1.0
    c = (float(i[3]+i[4]+i[5]) / 5.0) % 1.0
    d = (float(i[4]+i[5]+i[6]) / 7.0) % 1.0
    e = (float(i[5]+i[6]+i[7]) / 11.0) % 1.0
    f = (float(i[6]+i[7]+i[8]) / 13.0) % 1.0
    g = (float(i[7]+i[8]+i[9]) / 17.0) % 1.0
    if a==0 and b==0 and c==0 and d==0 and e==0 and f==0 and g==0:
        counter += float("".join(i))
print counter
