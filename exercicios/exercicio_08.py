# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

base = float(input("Digite a base do cálculo: "))
expoente = float(input("Digite o expoente: "))
potencia = base ** expoente

print(f'O número {base} elevado à {int(expoente)}ª potência corresponde a {potencia:.2f}.')