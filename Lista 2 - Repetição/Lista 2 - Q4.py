vezes = int(input())

for n in range(vezes):
    entrada = input().split()
    x = int(entrada[0])
    y = int(entrada[1])
    imp = 0
    result = 0
    while imp < y:
        if x % 2 != 0:
            result += x
            imp += 1
        x += 1
    print(result)

# Link para questão: https://imgur.com/a/1uwPLEW