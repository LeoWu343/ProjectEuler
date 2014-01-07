total = 0
for i in range(1, 100):
    for j in range(1, 100):
        curr = i ** j
        if len(str(curr)) == j:
            total += 1
print total
