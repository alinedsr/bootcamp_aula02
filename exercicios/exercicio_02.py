# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
print("------ Divisor por 5 ------")
DIVISOR = 5
numero = int(input("Digite um número inteiro: "))
resto = numero % DIVISOR
print(f'O resto da divisão entre {numero} e {DIVISOR} é {resto}.')