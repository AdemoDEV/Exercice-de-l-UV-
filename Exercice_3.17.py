x = float(input())
constante = 1e-6          
somme = 0.0             
termes = x 
n = 0
while abs(termes) >= constante:
    somme += termes
    n += 1
    termes *= -(x*x) / ((2*n) * (2*n + 1))
print(somme)
