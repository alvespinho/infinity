from funcoes import *
from time import sleep

while True:
    print("-"*50)
    oper = input ('''Calculadora
--------------------------------------------------                  
Escolha operação matemática ( + | - | * |  / | ** | sair): ''')

    if oper == '+':
        try:
            num1 = float(input('Número 1: '))
            num2 = float(input ('Número 2: '))
            print(num1, "+", num2, "=", somar(num1, num2))
            sleep(1.5)
        except:
            print("Erro de valor, digite um número válido.")
            sleep(1.5)
    elif oper == '-':
        try:
            num1 = float(input('Número 1: '))
            num2 = float(input('Número 2: '))
            print(num1, "-", num2, "=", subtrair(num1, num2))
            sleep(1.5)
        except:
            print("Erro de valor, digite um número válido.")
            sleep(1.5)        
    elif oper == '*':
        try:
            num1 = float(input('Número 1: '))
            num2 = float(input('Número 2: '))
            print(num1, "*", num2, "=", multiplicar(num1, num2))
            sleep(1.5)
        except:
            print("Erro de valor, digite um número válido.")
            sleep(1.5)
    elif oper == '/':
        try:
            num1 = float(input('Número 1: '))
            num2 = float(input('Número 2: '))
            print(num1, "/", num2, "=", dividir(num1, num2))
            sleep(1.5)
        except:
            print("Erro de valor, digite um número válido.")
            sleep(1.5)
    elif oper == '**':
        try:
            num1 = float(input('Número 1: '))
            num2 = float(input('Número 2: '))
            print(num1, "**", num2, "=", potencia (num1, num2))
            sleep(1.5)
        except:
            print("Erro de valor, digite um número válido.")
            sleep(1.5)
    elif oper == 'sair':
        print("Saindo do programa")
        sleep(1.5)
        break






