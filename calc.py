import math

def calculador():
    print ('### CALCULADORA SIMPLES ###')
    print ('[+] [-] [*] [/] [**] [sqrt]')

    while True:
        try:
            num1 = float (input('\nInsira 1° número: '))
            operador = input ('Operação: ')
            if operador.lower() == 'sqrt':
                if num1 < 0:
                    raise ValueError ('\nERRO: Impossível extrair raiz quadrada de número negativo!')
                result = math.sqrt(num1)
                return f'\nsqrt({num1}) = {result}'
            elif operador in ['+', '-', '*', '/', '**']:
                num2 = float (input('Insira 2° número: '))

                if operador == '+':
                    result = num1 + num2
                elif operador == '-':
                    result = num1 + num2
                elif operador == '*':
                    result = num1 * num2
                elif operador == '/':
                    if num2 != 0:
                        result = num1 / num2
                    else:
                        raise ValueError ('\nERRO: Divisão por 0 não permitida.')
                elif operador == '**':
                    result = num1 ** num2
            else:
                raise ValueError ('\nERRO: Operador inválido. Insira um operador válido.')
            return f'\n{num1} {operador} {num2} = {result}'
        except ValueError as e:
            mensagem_erro = str(e)
            if 'could not convert string to float' in mensagem_erro:
                print ('ERRO: Número inválido. Insira um número válido. \nTente novamente.')
            elif 'sqrt' in mensagem_erro:
                print (f'{mensagem_erro}')
            elif 'Division by zero' in mensagem_erro:
                print (f'{mensagem_erro}')
            elif 'Invalid operator' in mensagem_erro:
                print (f'{mensagem_erro}')
            else:
                print (f'{mensagem_erro} \nTente Novamente.')

print (calculador())



