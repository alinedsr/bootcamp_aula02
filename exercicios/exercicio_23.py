# 23: Calculadora Simples

try:
    nro1 = float(input("Digite o primeiro número: "))
    operador = input("Digite o operador: ")
    nro2 = float(input("Digite o segundo número: "))

    if operador == '+':
        print(nro1 + nro2)
    elif operador == '-':
        print(nro1 - nro2)
    elif operador == '*':
        print(nro1 * nro2)
    elif operador == '/':
        print(nro1 / nro2)
    else:
        print("O operador informado não é válido.")
except:
    print("Erro: Entrada inválida. Certifique-se de inserir números.")