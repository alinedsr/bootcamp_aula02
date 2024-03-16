# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

print("------ Divisão ------")
nro1 = int(input("Digite o primeiro número: "))
nro2 = int(input("Digite o segundo número: "))

try:
    divisao = nro1 / nro2
    divisao_inteira = nro1 // nro2
    print(f'O resultado da divisão entre {nro1} e {nro2} é {divisao}, enquanto o resultado da divisão inteira é {divisao_inteira}.')
except:
    print("Não é possível realizar divisão por zero.")