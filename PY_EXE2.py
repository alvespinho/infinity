#### PEDIR DOIS NÚMEROS E IMPRIMIR O MAIOR
'''
num1 = int (input ('Digite o primeiro número: '))
num2 = int (input ('Digite o segundo número: '))
if num1 == num2:
    print (F'{num1} e {num2} são iguais')
elif num1 > num2:
    print (F'{num1} é maior que {num2}')
else: 
    print (F'{num1} é menor que {num2}')
'''

#### VALOR NEGATIVO OU POSITIVO


#### MASCULINO OU FEMININO??


#### VOGAL OU CONSOANTE??
''' 
letra = str (input ('Digite uma Letra: '))
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print ('Esta Letra é Vogal')
elif letra == letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
    print ('Esta Letra é Vogal')
else:
    print ('Esta Letra é Consoante')
'''    
    

#### MÉDIA DO ALUNO
'''
nome_aluno = input('Digite o nome do aluno: ')
nota1 = float (input('Digite Nota 1: '))
nota2 = float (input('Digite Nota 2: '))
nota3 = float (input('Digite Nota 3: '))
nota4 = float (input('Digite Nota 4: '))
media = (nota1 + nota2 + nota3 + nota4)/ 4 
print (nome_aluno+ ', sua média é', media)
if media == 10:
    print(F'Parabéns, {nome_aluno}, você está APROVADO COM DISTINÇÃO')
elif media >= 7:
    print (F'Parabéns, {nome_aluno}, você está APROVADO')
else:
    print (F'Infelizmente, {nome_aluno}, você está REPROVADO')   
''' 
