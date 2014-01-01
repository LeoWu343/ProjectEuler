bigtotal = 0
for i in xrange(10, 999999): # doubt any numbers exist fulfilling the requirements past five digits (I mean six)
    diglist = list(str(i))
    total = 0
    for j in diglist:
        total += int(j) ** 5
    if i == total:
        bigtotal += total
print bigtotal
