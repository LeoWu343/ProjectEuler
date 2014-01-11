from fractions import Fraction as F
from operator import add

iterations = 1
multiple = 1
terms = [2]
while iterations != 100:
    terms.append(1)
    terms.append(2 * multiple)
    terms.append(1)
    multiple += 1
    iterations += 3

def start(insert):
    if insert == 99:
        return terms[99]
    return (terms[insert] + F(1, start(insert+1)))

print reduce(add, [int(i) for i in list(str(start(0).numerator))])
