from __future__ import generators
import itertools
import math

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

def unique(l):
    seen = set()
    seen_add = seen.add
    return [x for x in l if x not in seen and not seen_add(x)]

def equidistant(comparison, num1, num2):
    if math.fabs(num1-comparison) == math.fabs(num2-comparison):
        return True
    return False

visited = set()
visited_triples = set()
sieve = set(eratosthenes(10000))
for i in xrange(1000, 10000):
    nums = list(itertools.permutations(str(i)))
    nums = [int(''.join(a)) for a in nums]
    nums = sorted(unique(nums))
    if tuple(nums) not in visited:
        visited.add(tuple(nums))
    else:
        continue
    nums = [i for i in nums if i >= 1000]
    for i in xrange(len(nums)):
        for j in xrange(i+1, len(nums)):
            for k in xrange(j+1, len(nums)):
                if (nums[i], nums[j], nums[k]) in visited_triples:
                    continue
                else:
                    visited_triples.add((nums[i], nums[j], nums[k]))
                if equidistant(nums[j], nums[i], nums[k]):
                    if nums[j] in sieve and nums[i] in sieve and nums[k] in sieve:
                        print (nums[i], nums[j], nums[k])
