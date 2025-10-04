import random
secret = random.randint(0, 100)

essais = 0
while essais < 6:
    essaie_donnee = int(input())
    essais += 1

    if essaie_donnee == secret:
        print(f"Gagné en {essais} essai(s) !")
        break
    if essais < 6:
        print("Trop grand" if essaie_donnee > secret else "Trop petit")
else:
    print(f"Perdu ! Le secret était {secret}")

