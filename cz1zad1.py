import math

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))

delta = (b ** 2) - (4 * a * c)

if delta > 0:
    print((-b - math.sqrt(delta)) / (2 * a))
    print((-b + math.sqrt(delta)) / (2 * a))

elif delta == 0:
    print(-b / (2 * a))

else:
    print("Brak miejsc zerowych.")
