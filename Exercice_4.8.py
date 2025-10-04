def factoriel(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def catalan(n : int):
    catalan_n = (factoriel(2*n) // (factoriel(n + 1) * factoriel(n)))
    return catalan_n