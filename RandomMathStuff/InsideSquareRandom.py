ten = 24624
lim = 99999
for x in xrange(ten, lim, 1):
    notEqual = True
    sq = x * x
    while notEqual:
        y = ((sq / ten) % ten)
        y = int(y)
        if y == x:
            notEqual = False
        sq = y
        print(sq)
