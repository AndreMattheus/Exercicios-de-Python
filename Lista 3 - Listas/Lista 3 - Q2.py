n= int(input())

valores_apostas = []
jogadores = []
total_apostas = 0

for i in range(n):
    valor, jogador = input().split()
    valor = int(valor)
    jogador = int(jogador)
    valores_apostas.append(valor)
    jogadores.append(jogador)
    total_apostas += valor

jogador_ganhador = int(input())
total_ganhador = 0
ganhadores = []

for i in range(n):
    if jogadores[i] == jogador_ganhador:
        total_ganhador += valores_apostas[i]
        ganhadores.append(i)

comes = total_apostas//10
restante_apostadores = total_apostas - comes

if total_ganhador > 0:
    print(f'Total: R$ {total_apostas}')
    
    total_distribuido = 0
    
    for i in ganhadores: 
        parte_ganhador = (valores_apostas[i] * restante_apostadores) // total_ganhador
        print(f'Apostador {i+1}: R$ {parte_ganhador}' )
        total_distribuido += parte_ganhador
        
    if total_distribuido < restante_apostadores:
        comes += restante_apostadores - total_distribuido
else:
    total_distribuido = 0
    
    for i in range(n):
        parte_apostador = (valores_apostas[i] * restante_apostadores)// total_apostas
        print(f'Apostador {i+1}: R$ {parte_apostador}' )
        total_distribuido += parte_apostador
        
    if total_distribuido < restante_apostadores:
        comes += restante_apostadores - total_distribuido
        
print(f'Bebidas e petiscos: R$ {comes}' )

# Link para questão: https://imgur.com/a/QUeTi4Q