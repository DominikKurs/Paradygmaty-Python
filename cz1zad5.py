import random

arr = [random.randint(1, 100) for _ in range(20)]

arr.sort()

print(sum(arr))
print(sum(arr) / len(arr))
