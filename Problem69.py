from fractions import gcd
import operator

totients = {}
for i in xrange(2, 1000001):
    totients[i] = float(i)/len([j for j in list(xrange(1, i)) if gcd(i, j) == 1])
print max(totients.iteritems(), key=operator.itemgetter(1))[0]
