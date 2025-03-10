base = int(input())

for i in range(base):
    valores = input().split()
    pa = int(valores[0])
    pb = int(valores[1])
    g1 = float(valores[2])/100
    g2 = float(valores[3])/100
    
    npa = pa
    npb = pb
    result = 0
    
    while npa <= npb:
        ca = int(npa * g1)
        cb = int(npb * g2)
        npa += ca
        npb += cb
        result += 1
        
        if result > 100:
            print('Mais de 1 seculo.')
            break
    if result <= 100:
        print(f'{result} anos.')

# Link para questão: https://imgur.com/a/ypvvdyw