from operator import add
import time
start = time.clock()

seen = set()
for i in range(1, 9999):
    for j in range(1, int(10000.0/i)):
        prod = i * j
        if ''.join(sorted(list(str(i) + str(j) + str(prod)))) == '123456789':
            if prod not in seen:
                seen.add(prod)
nums = list(seen)
total = reduce(add, nums)
print total

print time.clock()-start
