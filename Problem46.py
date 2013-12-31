from __future__ import generators

# taken from http://c2.com/cgi/wiki?SieveOfEratosthenesInManyProgrammingLanguages
def eratosthenes(maxnum):
    D = {}  # map composite integers to primes witnessing their compositeness
    q = 2   # first integer to test for primality
    while q <= maxnum:
        if q not in D:
            yield q       # not marked composite, must be prime
            D[q*q] = [q]  # first multiple of q not already marked
        else:
            for p in D[q]:  # move each witness to its next multiple
                D.setdefault(p+q,[]).append(p)
            del D[q]        # no longer need D[q], free memory
        q += 1

sieve = set(eratosthenes(100000)) # I doubt the number is greater than 100,000
done = False
i = 3
while not done:
    if i not in sieve:
        j = 1
        check = False
        while j*j < i:
            remainder = i - (2 * j * j)
            if remainder in sieve:
                check = True
            j += 1
        if not check:
            done = True
            print i
    i += 2
