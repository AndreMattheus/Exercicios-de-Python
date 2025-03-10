def fuso (partida, viagem, diferenca):
    chegada = partida + viagem + diferenca
    if chegada >= 24:
        chegada -= 24
    if chegada < 0:
        chegada +=24
    return f'Hora de saída: {partida}\n' \
    f'Hora de chegada: {chegada}'

S = int(input())
if 0 <= S <= 23:
    T = int(input())
    if 1 <= T <= 12:
        F = int(input())
        if -5 <= F <= 5:
            print(fuso(S, T, F))
        else:
            print('Valor impossível para diferença de horário')
    else:
        print('Valor impossível para tempo de viagem')
else:
    print('Valor impossível para horas')

# Link para questão: https://postimg.cc/LJT5qwrg