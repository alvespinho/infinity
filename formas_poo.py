from formas_poo2 import *

while True:
    print ('''
    Áreas & Perímetros:
        
        1. Círculo
        2. Retângulo 
        3. Triângulo
        4. Pentágono
        5. Hexágono
        6. Sair
    ''')

    choice = (input ('Escolha uma forma geométrica: '))

    if choice == '1':
        raio = get_float_input ('Digite o valor de raio do círculo: ')
        
        circulo_usuario = Circulo(raio)

        print (f'\nA área do círculo é {(circulo_usuario.area()):.2f}')
        print (f'\nA circunferência do círculo é {(circulo_usuario.circunferencia()):.2f}\n')

    elif choice == '2':
        base = get_float_input ('Digite o valor da base do quadrilátero: ')
        altura = get_float_input ('Digite o valor da altura do quadrilátero: ')

        retangulo_usuario = Retangulo (base, altura)

        print (f'\nA área do retângulo é {(retangulo_usuario.area()):.2f}')
        print (f'\nO perimetro do retângulo é {(retangulo_usuario.perimetro()):.2f}\n')

    elif choice == '3':
        while True:
            try:  
                ladoa = get_float_input ('\nDigite o valor do lado A: ')
                ladob = get_float_input ('Digite o valor do lado B: ')
                ladoc = get_float_input ('Digite o valor do lado C: ')

                if (ladoa + ladob <= ladoc or ladoa + ladoc <= ladob or ladob + ladoc <= ladoa):
                    raise ValueError ('\nTriângulo inválido. Porfavor, insira medidas válidas para um Triângulo!')
                                                        
                else:
                    triangulo = Triangulo(ladoa, ladob, ladoc)
                    
                    if ladoa == ladob == ladoc:
                        tipo_tri = 'equilátero'
                    elif ladoa == ladob or ladoa == ladoc or ladob == ladoc:
                        tipo_tri = 'isósceles'
                    else:
                        tipo_tri = 'escaleno'

                    print(f'\nO triângulo é {tipo_tri} e tem área de: {triangulo.area():.2f}')
                    print(f'O triângulo é {tipo_tri} e tem perímetro de: {triangulo.perimetro():.2f}')
                    break
            except ValueError as e:
                print (e)
            

    elif choice == '4':
        pass
    elif choice == '5':
        pass
    elif choice == '6':
        break
    else: 
        print ('\nOpção inválida. Tente novamente.')


