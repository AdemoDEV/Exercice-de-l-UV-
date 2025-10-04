import random

s = int(input())
random.seed(s)

Nom = ["Pierre", "Feuille", "Ciseaux"]
Point_ordinateur = 0
Point_joueur = 0
IMPRIME = []    
    
def bat(joueur_1, joueur_2):
    global Point_ordinateur, Point_joueur
    if joueur_1 == joueur_2:
        IMPRIME.append(f"{Nom[joueur_1]} annule {Nom[joueur_2]} : {Point_joueur}")
    elif (joueur_1 - joueur_2) % 3 == 1:
        Point_joueur -= 1
        Point_ordinateur += 1
        IMPRIME.append(f"{Nom[joueur_1]} bat {Nom[joueur_2]} : {Point_joueur}")
    else:
        Point_joueur += 1
        Point_ordinateur -= 1
        IMPRIME.append(f"{Nom[joueur_1]} est battu par {Nom[joueur_2]} : {Point_joueur}")
        
manche = 0
while manche < 5:
     manche += 1
     ordinateur = random.randint(0,2)
     joueur = int(input())
     bat(ordinateur, joueur)
for ligne in IMPRIME:
    print(ligne)
if Point_joueur > Point_ordinateur:
    print("Gagné")
elif Point_joueur < Point_ordinateur:
    print("Perdu")
else:
    print("Nul")
    