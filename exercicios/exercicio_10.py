# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
import math
raio = float(input("Digite o raio do círculo: "))
area = (math.pi * (raio ** 2))

print(f'A área de um círculo com {raio} de raio corresponde a {area:.2f}.')