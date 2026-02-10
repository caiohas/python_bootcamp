## EXERCICIOS AULA 02: TypeError, Type Check, Type Conversion, try-except e if

# Parte 02: float
# 6) Escreva um programa que receba dois números flutuantes e realize sua adição.
num1 = float(input('Insira um numero float: '))
num2 = float(input('Insira um outro numero float: '))
print(f'A soma dos dois numeros é: {num1 + num2}')

# 7) Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
num1 = float(input('Insira um numero float: '))
num2 = float(input('Insira um outro numero float: '))
media = float(num1 + num2) / 2
print(f'A media dos dois numeros é: {media}')

# 8) Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
base = float(input('Insira a base da potencia: '))
expoente = float(input('Insira o expoente da potencia: '))
potencia = base ** expoente
print(f'O resultado da potencia de base {base} e {expoente} é: {potencia}')

# 9) Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C é igual a {fahrenheit}°F")

# 10) Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio = float(input('Informe o valor do raio do circulo para calculo de sua area: '))
area = 3.14 * (raio ** 2)
print(f'O valor da area de um circulo de raio {raio} é: {area}')