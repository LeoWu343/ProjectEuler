from __future__ import generators
import itertools
import time

start = time.clock()

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

def obviously_composite(i):
    for j in xrange(2, 21):
        if float(i) % float(j) == 0:
            return True
    return False

sieve = set(eratosthenes(7654321))
def find_primes(digits):
    diglist = list(itertools.permutations(digits))
    diglist = [int(''.join(i)) for i in diglist]
    diglist = [i for i in diglist if not obviously_composite(i) and i in sieve]
    if diglist:
        return diglist
    return find_primes(digits[1:])

print max(find_primes("987654321"))
print time.clock() - start
