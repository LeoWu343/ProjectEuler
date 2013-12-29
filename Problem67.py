f = open("Problem67.txt")
lines = f.readlines()

def memo(f):
    cache = {}
    def memoized(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return memoized

@memo
def solve(linenum, index):
    line = [int(i) for i in lines[linenum].split()]
    if linenum == 0:
        return line[0]
    if index >= 0 and index < len(line):
        return max(solve(linenum-1, index-1)+line[index], solve(linenum-1, index)+line[index])
    else:
        return float("-inf")

for i in xrange(len(lines)):
    for j in xrange(len(lines[i].split())):
        solve(i, j)
print max([solve(len(lines)-1, i) for i in xrange(len(lines[len(lines)-1].split()))])
