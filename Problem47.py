def memo(f):
    cache = {}
    def memoized(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return memoized

@memo
def factor(n):
    factors = []
    i = 2
    while i*i < n:
        while n % i == 0:
            n = n / i
            factors.append(i)
        i = i + 1
    factors.append(n)
    return factors

done = False
i = [1,2,3,4]
while not done:
    if len(set(factor(i[0]))) == 4 and all(len(set(factor(i[x]))) == len(set(factor(i[0]))) for x in range(len(i))):
        print i
        done = True
    i = [x+1 for x in i]
