ordem = int(input())

for n in range(1, ordem+1):
    aux = n
    inc = False
    lista = []
    for o in range(1, ordem+1):
        if inc == True:
            aux += 1
        elif aux-1 == 0:
            inc = True
          
        lista.append(aux)
        if inc == False:
            aux -= 1 
    print(' '.join(map(str,lista)))

# Link para questão: https://imgur.com/a/qUlH2pd