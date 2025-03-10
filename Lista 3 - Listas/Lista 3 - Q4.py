def linear(lista):
    lista_linear = []
    for i in lista:
        if isinstance(i, list):
            lista_linear.extend(linear(i))
        else:
            lista_linear.append(i)
    return lista_linear

lista_biblioteca = input()
lista_nova = eval(lista_biblioteca)
lista_linear = linear(lista_nova)

print(lista_linear)

# Link para questão: https://imgur.com/a/FZcDR0M