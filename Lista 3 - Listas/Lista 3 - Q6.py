n = int(input())

for fila in range(n):
    alunos = int(input())
    notas_sequencia = []
    notas_aluno = input().split()
    notas_aluno = list(map(int, notas_aluno))
    ntroca = 0
    for i in notas_aluno:
        notas_sequencia.append(i)
    notas_sequencia = sorted(notas_sequencia, reverse= True)
    for i in range(len(notas_aluno)):
        if notas_aluno[i] == notas_sequencia[i]:
            ntroca += 1
    
    print(ntroca)

# Link para questão: https://postimg.cc/WD2bm8MF