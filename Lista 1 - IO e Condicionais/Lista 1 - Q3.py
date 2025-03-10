def temperatura(valor, escala):
    if escala == 'C':
        celsius = valor
        fahrenheit = (valor * 9/5) + 32
        kelvin = valor + 273.15
    elif escala == 'F':
        celsius = (valor - 32) * 5/9
        fahrenheit = valor
        kelvin = (valor - 32) * 5/9 + 273.15
    elif escala == 'K':
        celsius = valor - 273.15
        fahrenheit = (valor - 273.15) * 9/5 + 32
        kelvin = valor
    
    return f"Temperatura em Celsius: {celsius:.2f} °C\n" \
           f"Temperatura em Fahrenheit: {fahrenheit:.2f} °F\n" \
           f"Temperatura em Kelvin: {kelvin:.2f} K"

entrada = input()
valor, escala = entrada.split()
valor = float(valor)
escala = escala.upper()

resultado = temperatura(valor, escala)
print(resultado)

# Link para questão: https://imgur.com/a/Ruvhtk8