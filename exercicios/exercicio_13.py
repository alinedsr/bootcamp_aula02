# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = input("Digite uma frase: ")
frase_sem_espacos = frase.strip()

print("Frase sem espaços no início e no final:", frase_sem_espacos)