arr = [
	[66, 97, 114, 100, 4, 2, 110, 11, 1, 6, 20],
	[99, 3, 10, 122, 76, 101, 111, 3, 32, 100, 0],
	[6, 22, 1, 111, 32, 10, 110, 7, 97, 97, 67],
	[60, 97, 116, 32, 100, 23, 97, 114, 100, 32, 34],
	[2, 106, 15, 6, 111, 56, 80, 20, 10, 86, 10],
	[20, 110, 121, 32, 107, 55, 50, 99, 110, 105, 8],
	[12, 9, 22, 102, 66, 100, 12, 105, 50, 76, 110],
	[42, 81, 123, 92, 26, 98, 20, 1, 20, 11, 10],
]

encoding = "rrrdddllddrrruuuurrddrruurddddlld"

x = 0
y = 0
haslomaslo = chr(arr[y][x])

for litera in encoding:
    if litera == "r":
        x += 1
    elif litera == "l":
        x -= 1
    elif litera == "d":
        y += 1
    elif litera == "u":
        y -= 1
    haslomaslo += chr(arr[y][x])

print(haslomaslo)
