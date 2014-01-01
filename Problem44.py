import sys
import time

start = time.clock()

pentagons = []
for i in range(1, 10001):
    pentagons.append((i*((3*i)-1))/2)
p = set(pentagons)

for j in range(len(pentagons)):
    for k in range(j, len(pentagons)):
        if pentagons[j]+pentagons[k] in p and pentagons[k]-pentagons[j] in p:
            print pentagons[k]-pentagons[j]
            print time.clock() - start
            sys.exit()
