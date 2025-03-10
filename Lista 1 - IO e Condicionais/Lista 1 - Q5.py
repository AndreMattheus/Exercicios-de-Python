entrada = input().split()
for x in range(len(entrada)):
    entrada[x] = float(entrada[x])

entrada.sort(reverse=True)
A = entrada[0]
B = entrada[1]
C = entrada[2]

if A >= B + C:
    print('NAO FORMA TRIANGULO')
else:
    if A**2 == B**2 + C**2:
        print('TRIANGULO RETANGULO')
    elif A**2 > B**2 + C**2:
        print('TRIANGULO OBTUSANGULO')
    elif A**2 < B**2 + C**2:
        print('TRIANGULO ACUTANGULO')
    
    if A == B == C:
        print('TRIANGULO EQUILATERO')
    elif A == B or B == C or A == C: 
        print('TRIANGULO ISOSCELES')

# Link para questão: https://imgur.com/a/mM4Nn4W