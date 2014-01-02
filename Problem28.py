total = 0
i = 1
increment = 2
curr = 0
while i <= 1001*1001:
    if curr == 4:
        increment += 2
        curr = 0
    total += i
    i += increment
    curr += 1

print total
