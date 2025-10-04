lever_soleil_E1515 = int(input())
coucher_soleil_E1515 = int(input())
lever_soleil_E666 = int(input())
coucher_soleil_E666 = int(input())


def soleil_leve(lever, coucher, heure):
    if lever == coucher:
        if lever == 0:
            return True
        if lever == 12:
            return False
        return False
    if lever < coucher:
        return lever <= heure < coucher
    return (heure >= lever) or (heure < coucher)

for i in range(23+1):
    E1515 = soleil_leve(lever_soleil_E1515, coucher_soleil_E1515, i)
    E666 = soleil_leve(lever_soleil_E666, coucher_soleil_E666, i)
    
    if not E1515 and not E666:
        print(f"{i} *")
    else:
        print(i)


