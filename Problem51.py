i = 1
done = False
while not done:
    digits = sorted(str(i))
    if sorted(str(2 * i)) == digits and sorted(str(3 * i)) == digits and sorted(str(4 * i)) == digits and sorted(str(5 * i)) == digits and sorted(str(6 * i)) == digits:
        print i
        done = True
    i += 1
