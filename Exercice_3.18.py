n = int(input())
for i in range(1, n + 1):
    espaces = n - i
    if espaces > 0:
        print(" " * espaces, end="")
    milieu = i
    for j in range(1, milieu + 1):
        print((i + j - 1) % 10, end="")
    for j in range(milieu - 1, 0, -1):
        print((i + j - 1) % 10, end="")
    print()