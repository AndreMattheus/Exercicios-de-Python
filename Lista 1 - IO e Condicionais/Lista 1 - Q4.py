coord = input().split()
for i in range(len(coord)):
    coord[i] = int(coord[i])
    
x1 = coord[0]
y1 = coord[1]
x2 = coord[2]
y2 = coord[3]

ponto = input().split()
for i in range(len(ponto)):
    ponto[i] = int(ponto[i])
    
x = ponto[0]
y = ponto[1]

if (x < x1 or x > x2) or (y < y1 or y > y2):
    print('Fora!')
else:
    print('Dentro!')

# Link para questão: https://imgur.com/a/obYAx7S