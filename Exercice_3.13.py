total = 0
first = int(input())

if first == -1:
    while True:
        data = input().strip()
        if data == "F":
            break
        total += int(data)
else:
    for _ in range(first):
        total += int(input())

print(total)
