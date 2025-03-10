num = int(input())
fat = 1

if num <= 0:
    print('O número deve ser maior que 0.')
else:
    for i in range(1, num+1):
        fat = i * fat
    print(f'Resultado do fatorial: {fat}')

# Link para questão: https://imgur.com/a/opPe4XT