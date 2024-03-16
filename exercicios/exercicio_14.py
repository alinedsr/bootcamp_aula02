# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

data = input("Digite uma data, no formato dd/mm/yyyy: ")
data_separada = data.split("/")
dia = data_separada[0]
mes = data_separada[1]
ano = data_separada[2]

print(f'Dia {dia}, mês {mes}, ano {ano}.')