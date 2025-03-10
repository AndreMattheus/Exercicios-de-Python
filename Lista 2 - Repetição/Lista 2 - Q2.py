gastos = []
num = None

while num != 0:
    num = float(input())
    gastos.append(num)

if len(gastos) == 1:
    print('Você não teve gastos hoje!')
else:
    print(f'O seu maior gasto hoje foi R$ {max(gastos):.2f}')

# Link para questão: https://imgur.com/a/lWKTiib