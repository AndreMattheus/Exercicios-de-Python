valores = input().split(',')
valores = list(map(float,valores))


if len(valores) < 2:
    print('Não é possível determinar o segundo maior valor com menos de dois elementos.')
    
elif valores[1] == None or valores[1] == valores[0]:
    print('Não é possível determinar o segundo maior valor com menos de dois valores distintos.')

else:
    print(sorted(set(valores), reverse=True)[1])

# Link para questão: https://imgur.com/a/Ry2RRSa