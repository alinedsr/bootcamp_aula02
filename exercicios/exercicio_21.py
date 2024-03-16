# 21: Conversor de Temperatura

temperatura = float(input("Digite a temperatura que gostaria de converter: "))
print("Em qual escala a temperatura foi informada?")
escala_termometrica_entrada = input("Digite C para Celsius, K para Kelvin ou F para Fahrenheit: ")
escala_termometrica_entrada = escala_termometrica_entrada.upper()
print("Para qual escala gostaria de converter a temperatura informada?")
escala_termometrica_conversao = input("Digite C para Celsius, K para Kelvin ou F para Fahrenheit: ")
escala_termometrica_conversao = escala_termometrica_conversao.upper()

if (escala_termometrica_entrada == 'C' and escala_termometrica_conversao == 'C') or (escala_termometrica_entrada == 'K' and escala_termometrica_conversao == 'K') or (escala_termometrica_entrada == 'F' and escala_termometrica_conversao == 'F'):
    print("Não é possível converter pois as escalas informadas são iguais.")
elif escala_termometrica_entrada == 'C' and escala_termometrica_conversao == 'K':
    temperatura_convertida = temperatura + 273.15
    print("Temperatura convertida:", temperatura_convertida)
elif escala_termometrica_entrada == 'C' and escala_termometrica_conversao == 'F':
    temperatura_convertida = (temperatura * 1.8) + 32
    print("Temperatura convertida:", temperatura_convertida)
elif escala_termometrica_entrada == 'K' and escala_termometrica_conversao == 'C':
    temperatura_convertida = temperatura - 273,15
    print("Temperatura convertida:", temperatura_convertida)
elif escala_termometrica_entrada == 'K' and escala_termometrica_conversao == 'F':
    temperatura_convertida = (temperatura *9) / 5 + 459.67
    print("Temperatura convertida:", temperatura_convertida)
elif escala_termometrica_entrada == 'F' and escala_termometrica_conversao == 'C':
    temperatura_convertida = (temperatura - 32) / 1.8
    print("Temperatura convertida:", temperatura_convertida)
elif escala_termometrica_entrada == 'F' and escala_termometrica_conversao == 'K':
    temperatura_convertida = (temperatura + 459.67) * 5 / 9
    print("Temperatura convertida:", temperatura_convertida)