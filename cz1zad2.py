def silnia(n):
    if n == 0:
        return 1
    return n * silnia(n - 1)

print(silnia(5))