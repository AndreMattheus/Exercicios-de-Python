lista = input()
lista = lista.strip('[')
lista = lista.strip(']')
lista = lista.replace(' ','')
lista = lista.split(',')
antigo = input()
substituir = input()

if antigo in lista:
    for i in range(len(lista)):
        if lista[i] == antigo:
            lista[i] = substituir
    print(lista)
else:
    print('Item não presente no inventário.')

# Link para questão: https://imgur.com/a/9bOAqVm