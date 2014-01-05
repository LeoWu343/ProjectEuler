import math

def nCr(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n-r))

total = 0
for i in xrange(1, 101):
    for j in xrange(1, i+1):
        if nCr(i, j) > 1000000:
            total += 1
print total
