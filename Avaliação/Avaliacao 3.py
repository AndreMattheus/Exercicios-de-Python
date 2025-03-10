N = int(input())
aux = 0
numeros = []
numeros.append(0)
if 0 <= N <= 200:
    while aux < N+1:
        for i in range(aux):
            numeros.append(aux)
        aux += 1
print(f'{len(numeros)} números')
numeros = map(str, numeros)
print(' '.join(numeros))

# Link para questão: https://postimg.cc/B8dwDSLm