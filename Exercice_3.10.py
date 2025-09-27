total = 0
nombre = 0

salaire = int(input())
while salaire != -1:
    total += salaire
    nombre += 1
    salaire = int(input())

print(total / nombre)
