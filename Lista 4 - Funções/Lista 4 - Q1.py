def verifyprimo (num):
    Primo = True
    if num >= 2:
        for i in range(2, num):
            if num % i == 0:
                return False
            else:
                return True

n = int(input())
if n >= 0:
    if verifyprimo(n) == True:
        if verifyprimo(n+2) == True:
            print(f'Número forma par de gêmeos')
        else:
            print(f'Número não forma par de gêmeos')
    else:
        print(f'Número não forma par de gêmeos')
else:
    print(f'Número não é inteiro positivo')

# Link para questão: https://postimg.cc/Q96d67X8