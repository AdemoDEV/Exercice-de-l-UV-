import random
NB_ESSAIS_MAX = 6
secret = random.randint(0, 100)

essais = 0
while essais < NB_ESSAIS_MAX:
    essaie_donnee = int(input())
    essais += 1

    if essaie_donnee == secret:
        print(f"Gagné en {essais} essai(s) !")
        break
    if essais < NB_ESSAIS_MAX:
        print("Trop grand" if essaie_donnee > secret else "Trop petit")
else:
    print(f"Perdu ! Le secret était {secret}")
