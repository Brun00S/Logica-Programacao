escala= input("Você vai digitar a temperatura em qual escala? ")

celsius = (escala == "C" or escala == "c")
fahrenheit = (escala == "F") or (escala =="f")

valor_fahrenheit = 0
valor_celsius = 0



if fahrenheit:
    valor_fahrenheit = input("Digite a temperatura em Fahrenheit: ")
    valor_fahrenheit_float = float(valor_fahrenheit)
    valor_celsius = ((valor_fahrenheit_float - 32) * 5) / 9
    print(f'Temperatura equivalente em Celsius: {valor_celsius:.2f}')
elif celsius:
    valor_celsius = input("Digite a temperatura em Celsius: ")
    valor_celsius_float = float(valor_celsius)
    valor_fahrenheit = ((valor_celsius_float * 9) + 160) / 5
    print(f'Temperatura equivalente em Fahrenheit: {valor_fahrenheit:.2f}')