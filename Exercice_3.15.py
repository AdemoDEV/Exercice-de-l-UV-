saut = int(input())
position_cible = int(input())
position_courante = 0

while True:
    position_courante = (position_courante + saut) % 100
    
    if position_courante == 0:
        print(0)
        print("Pas trouvée")
        break
    
    if position_courante == position_cible:
        print("Cible atteinte")
        break
    
    print(position_courante)
