def get_range (n, cells, distance, user):
    indices = []
    for i in range(n):
        if abs(cells[i] - user) <= distance:
            indices.append(cells[i])
    return indices

N, D, U = map(int, input().split())
cells = [int(input()) for _ in range(N)]

indices = get_range(N, cells, D, U)

if indices:
    print(" ".join(map(str, indices)))
else:
    print('USUARIO DESCONECTADO')

# Link para questão: https://postimg.cc/6y6nMVtZ