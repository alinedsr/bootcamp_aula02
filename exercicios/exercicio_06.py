# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

try:
    nro1 = float(input("Digite o primeiro número: "))
except:
    print("O valor digitado não é um número válido. Por favor, utilize ponto como separador de casa decimal.")

try:
    nro2 = float(input("Digite o segundo número: "))
except:
    print("O valor digitado não é um número válido. Por favor, utilize ponto como separador de casa decimal.")

try:
    soma = nro1 + nro2
    print(f'O resultado da soma entre {nro1} e {nro2} é {soma}.')
except:
    print("Não é possível realizar a operação com os valores fornecidos.")
