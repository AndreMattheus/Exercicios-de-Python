preco = float(input())
metodo = input()

desconto = int(preco * 0.95)
extra = int(preco * 1.08)
parcelas = int(extra / 3)

if metodo == 'V' :
    print(f'Valor à pagar: {desconto}')
elif metodo == 'P' :
    print(f'Valor à pagar: {extra}') 
    print(f'Parcela 1: {parcelas}') 
    print(f'Parcela 2: {parcelas}') 
    print(f'Parcela 3: {parcelas}') 

# Link para questão: https://imgur.com/a/6Zi1Ubj