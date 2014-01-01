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

primes = list(eratosthenes(999999)) # doubt numbers will go past a million - will change if necessary
sieve = set(eratosthenes(999999))
total = 0
fulfillers = []
for i in primes:
    if i < 10:
        continue
    stri = str(i)
    trunc = True
    for j in range(len(stri)):
        curr1 = stri[j:]
        curr2 = stri[:len(stri)-j]
        if int(curr1) not in sieve or int(curr2) not in sieve:
            trunc = False
    if trunc:
        total += i
        fulfillers.append(i)

print total
print fulfillers
