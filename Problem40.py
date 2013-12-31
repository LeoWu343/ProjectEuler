a = ""
i = 1
while len(a) < 1000000:
    a += str(i)
    i += 1

print int(a[1-1])*int(a[10-1])*int(a[100-1])*int(a[1000-1])*int(a[10000-1])*int(a[100000-1])*int(a[1000000-1])
