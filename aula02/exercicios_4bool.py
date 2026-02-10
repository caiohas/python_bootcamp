# EXERCICIOS AULA 02: TypeError, Type Check, Type Conversion, try-except e if

# Parte 03: bool
# 16) Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# Exemplo de entrada
valor1 = True
valor2 = False
resultado_and = valor1 and valor2
print("Resultado do AND lógico:", resultado_and)

# 17) Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
valor1 = True
valor2 = False
resultado_or = valor1 or valor2
print("Resultado do OR lógico:", resultado_or)

# 18) Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
valor1 = True
resultado_not = not valor1
print("Resultado do NOT lógico:", resultado_not)

# 19) Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
num1 = int(input('Insira um numero inteiro: '))
num2 = int(input('Insira um outro numero inteiro: '))
resultado_igualdade = (num1 == num2)
print("Resultado da igualdade:", resultado_igualdade)

# 20) Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
num1 = int(input('Insira um numero inteiro: '))
num2 = int(input('Insira um outro numero inteiro: '))
resultado_diferenca = (num1 != num2)
print("Resultado da diferença:", resultado_diferenca)