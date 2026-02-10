# EXERCICIOS AULA 02: TypeError, Type Check, Type Conversion, try-except e if

# Parte 03: strings
# 11) Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
string = input('Digite uma frase... ')
print(f'Sua frase em maiusculo: {string.upper()}')

# 12) Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
string = input('Digite seu nome completo... ')
print(f'Seu nome em minusculo: {string.lower()}')

# 13) Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = "  Olá, mundo!  "  # Exemplo de entrada
frase_sem_espacos = frase.strip()
print("Frase sem espaços no início e no final:", frase_sem_espacos)

# 14) Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input("Digite uma data no formato dd/mm/aaaa: ")
dia, mes, ano = data.split("/")
print("Dia:", dia)
print("Mês:", mes)
print("Ano:", ano)

# 15) Escreva um programa que concatene duas strings fornecidas pelo usuário.
string1 = input('Digite uma frase... ')
string2 = input('Digite a continuacao dessa frase... ')
string_final = string1 + ' ' + string2
print(f'A frase concatenada é: {string_final}')