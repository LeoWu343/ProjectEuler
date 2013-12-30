counter = 0
for i in range(1, 1001):
    counter += long(i)**long(i) % long(10**10)
print counter % long(10**10)
