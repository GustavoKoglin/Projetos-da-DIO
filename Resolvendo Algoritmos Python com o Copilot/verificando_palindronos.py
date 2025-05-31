# -*- coding: utf-8 -*-

# Solicitamos uma palavra do usuário
palavra = input("Digite uma palavra: ")

# Verificamos se a palavra é um palíndromo invertendo a string
if palavra == palavra[::-1]:
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")
