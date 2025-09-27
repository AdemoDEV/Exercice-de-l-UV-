import math
nombre_1 = float(input())
nombre_2 = float(input())
if nombre_1 >= 0 and nombre_2 >= 0:
    print(math.sqrt(nombre_1*nombre_2))
else:
    print("Erreur")
