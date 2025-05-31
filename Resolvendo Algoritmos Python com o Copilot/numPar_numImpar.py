# -*- coding: utf-8 -*-

# Recebemos um número inteiro do usuário
numero = int(input("Digite um número inteiro: "))

# Verificamos se é par ou ímpar usando o operador de módulo (%)
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
