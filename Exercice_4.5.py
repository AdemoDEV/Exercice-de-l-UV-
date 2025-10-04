
def rendre_monnaie(prix, x20,x10,x5,x2,x1):
    x20_f, x10_f, x5_f, x2_f, x1_f = 20 * x20, 10 * x10, 5 * x5, 2 * x2, 1 * x1
    total_price = x20_f + x10_f + x5_f + x2_f + x1_f
    if total_price == prix:
         return 0,0,0,0,0
    elif total_price > prix:
        reste = total_price - prix
        billet_20 = reste // 20
        reste = reste % 20
        billet_10 = reste // 10
        reste = reste % 10
        billet_5 = reste // 5
        reste = reste % 5
        piece_2 = reste // 2
        reste = reste % 2
        piece_1 = reste // 1
        return billet_20, billet_10, billet_5, piece_2, piece_1
    else:
        return None, None, None, None, None
    