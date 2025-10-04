import random

def alea_dice(s):
    random.seed(s)
    de_1 = random.randint(1, 6)
    de_2 = random.randint(1, 6)
    de_3 = random.randint(1, 6)
    de_final = de_1 + de_2 + de_3
    if de_final == 7:
        return True
    else:   
        return False
        
        
print(alea_dice(468))