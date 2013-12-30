f = open("Problem42.txt")
words = f.readline()
words = words[1:len(words)-1].split('","')
triangles = set()
for i in range(1, 26 * (max(len(w) for w in words)+1)):
    triangles.add(0.5 * float(i) * float(i+1))
counter = 0
for w in words:
    wlist = list(w)
    wvalue = 0
    for c in wlist:
        wvalue += ord(c)-64
    if float(wvalue) in triangles:
        counter += 1
print counter
