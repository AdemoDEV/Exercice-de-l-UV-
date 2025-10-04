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
