'''
    Autores: Glauber Almeida B. - Luis Henrique Nunes C. P.
    Turma: 2ºA DS               Data: 28/08/2025

    Exercício 02
    - Faça um programa que leia um número entre 0 e 9999 e mostre:
    - Unidades
    - Dezenas
    - Centenas
    - Milhares
'''


# Solicita um número ao usuário. Para este código funcionar,
# o usuário DEVE digitar um número de 4 dígitos (ex: 0001, 0123, 1234).
numero_str = input("Digite um número de 4 dígitos (ex: 0123): ")

# Acessa cada caractere da string diretamente por seu índice
# A contagem do índice começa do 0.
milhares = numero_str[0]
centenas = numero_str[1]
dezenas = numero_str[2]
unidades = numero_str[3]

# Exibe o resultado
print(f"O número digitado foi {numero_str}.")
print(f"Milhares: {milhares}")
print(f"Centenas: {centenas}")
print(f"Dezenas: {dezenas}")
print(f"Unidades: {unidades}")





'''
num = str(input("digite um numero de 0 a 9999 (com 4 casas): ")) #Lê o Número que o usuário inseriu
caracteres = list(num) # separa os caracteres
# Exibição
print(f"Unidade: {caracteres[3]}")
print(f"Dezena: {caracteres[2]}")
print(f"Centenas: {caracteres[1]}")
print(f"Milhares: {caracteres[0]}")
'''
