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

num = str(input("digite um numero de 0 a 9999 (com 4 casas): "))
print(num)
caracteres = list(num)
print(f"Unidade: {caracteres[3]}")
print(f"Dezena: {caracteres[2]}")
print(f"Centenas: {caracteres[1]}")
print(f"Milhares: {caracteres[0]}")
