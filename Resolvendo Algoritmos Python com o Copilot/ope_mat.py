# -*- coding: utf-8 -*-

import math  # Importamos a biblioteca matemática para operações avançadas

# Funções para realizar operações matemáticas

def soma(x, y):
    """Retorna a soma de dois números"""
    return x + y

def subtracao(x, y):
    """Retorna a subtração entre dois números"""
    return x - y

def multiplicacao(x, y):
    """Retorna a multiplicação entre dois números"""
    return x * y

def divisao(x, y):
    """Retorna a divisão entre dois números, evitando divisão por zero"""
    return x / y if y != 0 else "Indefinida (divisão por zero)"

def potencia(x, y):
    """Retorna x elevado à potência de y"""
    return x ** y

def raiz_quadrada(x):
    """Retorna a raiz quadrada de um número, garantindo que ele não seja negativo"""
    return math.sqrt(x) if x >= 0 else "Indefinida (número negativo)"

def fatorial(x):
    """Retorna o fatorial de um número inteiro positivo"""
    return math.factorial(int(x)) if x >= 0 and x.is_integer() else "Indefinido"

def logaritmo(x):
    """Retorna o logaritmo natural (base e) de um número, garantindo que ele seja positivo"""
    return math.log(x) if x > 0 else "Indefinido"

def bhaskara(a, b, c):
    """Calcula as raízes de uma equação do segundo grau usando a fórmula de Bhaskara"""
    delta = b**2 - 4*a*c  # Calculamos o discriminante (delta)
    
    if delta >= 0:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    else:
        raiz1, raiz2 = "Raízes imaginárias", "Raízes imaginárias"

    return delta, raiz1, raiz2

# Loop principal para o usuário escolher operações até decidir sair
while True:
    # Exibimos o menu de opções
    print("\nEscolha uma operação matemática:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potenciação")
    print("6 - Raiz Quadrada")
    print("7 - Fatorial")
    print("8 - Logaritmo")
    print("9 - Fórmula de Bhaskara")
    print("0 - Sair")

    # Recebemos a opção do usuário
    opcao = input("Digite a opção desejada: ")

    # Caso o usuário queira sair, encerramos o programa
    if opcao == "0":
        print("Encerrando o programa. Até mais!")
        break

    # Operações que requerem dois números
    elif opcao in ["1", "2", "3", "4", "5"]:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        # Criamos um dicionário que mapeia cada opção para a função correspondente
        operacoes = {
            "1": soma,
            "2": subtracao,
            "3": multiplicacao,
            "4": divisao,
            "5": potencia
        }

        # Chamamos a função correspondente e exibimos o resultado
        resultado = operacoes[opcao](num1, num2)
        print(f"Resultado: {resultado}")

    # Operações que requerem apenas um número
    elif opcao in ["6", "7", "8"]:
        num = float(input("Digite um número: "))

        operacoes = {
            "6": raiz_quadrada,
            "7": fatorial,
            "8": logaritmo
        }

        resultado = operacoes[opcao](num)
        print(f"Resultado: {resultado}")

    # Operação para resolver equações do segundo grau
    elif opcao == "9":
        a = float(input("Digite o coeficiente a: "))
        b = float(input("Digite o coeficiente b: "))
        c = float(input("Digite o coeficiente c: "))

        delta, raiz1, raiz2 = bhaskara(a, b, c)
        print(f"Delta: {delta}")
        print(f"Raiz 1: {raiz1}")
        print(f"Raiz 2: {raiz2}")

    # Caso o usuário digite uma opção inválida
    else:
        print("Opção inválida! Escolha novamente.")

    # Perguntamos se o usuário quer continuar
    continuar = input("Deseja realizar outra operação? (s/n): ").lower()
    if continuar != "s":
        print("Encerrando o programa. Até mais!")
        break
