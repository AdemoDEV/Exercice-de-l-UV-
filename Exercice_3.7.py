parie = int(input()) 
tirage = int(input()) 
mise = 10

ROUGE = {1, 3, 5, 6, 7, 9, 12}
NOIR  = {2, 4, 8, 10, 11}

res = 0

if 0 <= parie <= 12:
    res = 12 * mise if tirage == parie else 0
elif parie == 13:            
    res = 2 * mise if tirage % 2 == 0 else 0
elif parie == 14:            
    res = 2 * mise if tirage % 2 == 1 else 0
elif parie == 15:            
    res = 2 * mise if tirage in ROUGE else 0
elif parie == 16:            
    res = 2 * mise if tirage in NOIR else 0

print(res)
