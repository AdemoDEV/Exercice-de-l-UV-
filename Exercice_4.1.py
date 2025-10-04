def deux_egaux(a, b, c):
    return (a == b) or (a == c) or (b == c)

x = int(input())
y = int(input())
z = int(input())

print(deux_egaux(x, y, z))