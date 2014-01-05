def isPalindrome(num):
    if int(str(num)[::-1])==num:
        return True
    return False

def isLychrel(num, it):
    if it == 50:
        return True
    added = num + int(str(num)[::-1])
    if isPalindrome(added):
        return False
    return isLychrel(added, it+1)

total = 0
for i in xrange(1, 10000):
    if isLychrel(i, 1):
        total += 1
print total
