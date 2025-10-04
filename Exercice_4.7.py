import math

def rac_eq_2nd_deg(a : float, b : float, c : float):
    delta = b**2 - 4 * a * c
    if delta < 0:
        return ()
    elif delta > 0 :
        sol_1 = (-b - math.sqrt(delta)) / (2*a)
        sol_2 = (-b + math.sqrt(delta)) / (2*a)
        return min(sol_1, sol_2), max(sol_1, sol_2)
    else:
        sol_1 = -b / (2 * a)
        return sol_1,
    