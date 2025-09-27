import math
formule = str(input().upper())
nombre = float(input())
tableau = {
    "T": (math.sqrt(2) /12 ) * nombre**3,
    "C": nombre**3,
    "O": (math.sqrt(2) / 3) * nombre**3,
    "D": ((15+7*math.sqrt(5)) / 4) * nombre**3,
    "I": ((5*(3+math.sqrt(5))) / 12) * nombre**3
}

if tableau.get(formule) is not None:
    print(tableau.get(formule))
else:
    print("Polyèdre non connu")