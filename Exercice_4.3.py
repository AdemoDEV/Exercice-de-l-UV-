x = int(input())

def premier(nombre):
    for i in range(2, nombre): # Pourquoi 2 et pourquoi Nombre ? parce que tout nombre est divisible par 1 et pourquoi nombre parce que on sair déja que le nombre nombre est divisible par lui meme
        if nombre % i == 0:
            return False
    return True

for nombre in range(2, x):
    if premier(nombre):
        print(nombre)