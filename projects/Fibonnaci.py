def F(n):
    if n < 2:
        return n
    else:
        return F(n-2) + F(n-1)