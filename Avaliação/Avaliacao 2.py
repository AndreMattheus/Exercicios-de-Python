N = int(input())
coelhos = 0
ratos = 0
sapos = 0

for i in range(N):
    teste = input()
    valor, tipo = teste.split()
    valor = int(valor)
    
    if 1 <= valor <= 15:
        if tipo == 'C':
            coelhos = coelhos + valor
        elif tipo == 'R':
            ratos = ratos + valor
        elif tipo == 'S':
            sapos = sapos + valor 
        
total = coelhos + sapos + ratos
pcoelhos = (coelhos/total) * 100
pratos = (ratos/total) * 100
psapos = (sapos/total) * 100

print(f'Total: {total} cobaias\n' \
f'Total de coelhos: {coelhos}\n' \
f'Total de ratos: {ratos}\n' \
f'Total de sapos: {sapos}\n' \
f'Percentual de coelhos: {pcoelhos:.2f} %\n' \
f'Percentual de ratos: {pratos:.2f} %\n' \
f'Percentual de sapos: {psapos:.2f} %' )

# Link para questão: https://postimg.cc/gLp8F5Qz