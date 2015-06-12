from fractions import Fraction

def memo(f):
    cache = {}
    def memoized(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return memoized

@memo
def root_iter(n):
    if (n == 1):
        return 1 + Fraction(1, 2)
    else:
        return 1 + Fraction(1, root_iter(n-1) + 1)

total = 0
for i in range(1, 1001):
    curr = root_iter(i)
    if len(str(curr.numerator)) > len(str(curr.denominator)):
        total += 1

print total
