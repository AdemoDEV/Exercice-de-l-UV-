def bat(joueur_1, joueur_2):
    if joueur_1 == joueur_2:
        return False
    elif (joueur_1 - joueur_2) == -1 or (joueur_1 - joueur_2) == 2:
        return False
    elif (joueur_1 - joueur_2) == 1 or (joueur_1 - joueur_2) == -2:
        return True
    elif joueur_1 == 2 and joueur_2 == 0:
        return True
    
#ou

def bat(joueur_1, joueur_2):
    global Point_ordinateur, Point_joueur
    if joueur_1 == joueur_2:
        return False
    elif (joueur_1 - joueur_2) % 3 == 1:
        return True
    else:
        return False