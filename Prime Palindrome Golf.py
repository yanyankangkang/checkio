def golf(number):
    for i in range(number + 1, 99999):
        if (str(i) == str(i)[::-1] and all(i % j for j in xrange(2, i))):
            return i

print golf(13)
