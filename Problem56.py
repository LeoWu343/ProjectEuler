high = 0
for i in range(1, 100):
    for j in range(1, 100):
        total = 0
        curr = i ** j
        for k in list(str(curr)):
            total += int(k)
        if total > high:
            high = total
print high
