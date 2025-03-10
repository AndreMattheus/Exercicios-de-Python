def intervalo (email, arroba, ponto):
    arroba = email.find('@')
    ponto = email.find('.', arroba)
    return arroba, ponto

emails = []
while len(emails) < 50:
    email = input()
    if email == 'FIM':
        break
    emails.append(email)

for email in emails:
    arroba, ponto = intervalo(email, 0, 0)
    if arroba != -1 and ponto != -1:
        parte1 = email[arroba + 1 : ponto]
        print(parte1)
    else:
        print('Formato Invalido')

# Link para questão: https://postimg.cc/k6FwbnvP