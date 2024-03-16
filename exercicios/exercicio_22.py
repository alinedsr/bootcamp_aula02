# 22: Verificador de Palíndromo

texto = input("Digite um texto para verificação: ")
palindromo = texto[::-1]
print(palindromo)

if texto == palindromo:
    print("O texto informado é um palíndromo!")
else:
    print("O texto informado não é um palíndromo.")