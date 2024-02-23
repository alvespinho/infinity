# Exercício 01 - Faça um Programa que mostre a mensagem "Alo mundo" na tela.
print("Alo mundo")

# Exercício 02 - Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
num = float(input("Digite um número:\n"))
print(f"O número informado foi {num}")

# Exercício 03 - Faça um Programa que peça dois números e imprima a soma.
num1 = float(input("Digite o primeiro número:\n"))
num2 = float(input("Digite o segundo número:\n"))
soma = (num1 + num2)
print(f"A soma dos números é {soma}")

# Exercício 4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.
nota1 = float(input("Digite a primeira nota do bimestre:\n"))
nota2 = float(input("Digite a segunda nota do bimestre:\n"))
nota3 = float(input("Digite a terceira nota do bimestre:\n"))
nota4 = float(input("Digite a quarta nota do bimestre:\n"))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"A média do bimestre é igual a {media}")

# Exercício 5 - Faça um Programa que converta metros para centímetros.
num = float(input("Digite um número em metros:\n"))
cen = num * 100
print(f"{num} metros equivale a {cen} centímetros.")

# Exercício 6 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
raio = float(input("Digite o raio do círculo:\n"))
area = 3.14 * (raio * raio)
print(f'A área do raio é {area} metros quadrados')

# Exercícios 7 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
lado = float(input("Digite o lado do quadrado:\n"))
area = (lado * lado) * 2
print(f'O dobro da área do quadrado é {area}')

# Exercício 8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
valorHora = float(input('Quanto você recebe por hora trabalhada?\n'))
horaMes = float(input('Quantas horas você trabalha por mês?\n'))
salarioBruto = (valorHora * horaMes)
print(f'O seu salário bruto é R$ {salarioBruto} reais.')

# Exercício 9 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
grauF = float(input('Digite a temperatura em graus Fahrenheit:\n'))
grauC = (grauF - 32) / 1.8
print(f'A temperatura em Graus Celsius é {grauC}')

# Exercício 10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
grauC = float(input('Digite a temperatura em graus celsius:\n'))
grauF = (grauC * 1.8) + 32
print(f'A temperatura em Graus Fahrenheit é {grauF}')

# Exercício 11 - 
# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.
num1 = int(input('Digite o primeiro número inteiro:\n'))
num2 = int(input('Digite o segundo número inteiro:\n'))
num3 = float(input('Digite o número real:\n'))
produto = (num1*2) * (num2/2)
soma = (num1*3) + num3
elevado = (num3*num3*num3)
print(f'O produto do dobro do primeiro com a metade do segundo é igual a {produto}')
print(f'A soma do triplo do primeiro com o terceiro é igual a {soma}')
print(f'O terceiro elevado com cubo é igual a {elevado}')

# Exercício 12 - Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
altura = float(input('Digite a sua altura:\n'))
pesoIdeal = (72.7 * altura) - 58
print(f'O seu peso ideal é de {pesoIdeal}kg.')

# Exercício 13 - 
# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
altura = float(input('Digite a sua altura:\n'))
sexo = str(input('Digite "H" para homem e "M" para mulher:\n')).lower()
if sexo == 'h':
    pesoIdeal = (72.7 * altura) - 58
    print(f'O seu peso ideal de acordo com a sua altura é de {pesoIdeal}kg')
elif sexo == 'm':
    pesoIdeal = (62.1 * altura) - 44.7
    print(f'O seu peso ideal de acordo com a sua altura é de {pesoIdeal}kg')
    
# Exercício 14 -
# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
# deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes)
# e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.
peso = float(input('Digite o peso total do quilos de peixes:\n'))
pesoPeixe = 50
multa = 4
excessoPesoPeixe = (peso - pesoPeixe)
multaExcesso = (excessoPesoPeixe * multa)
print(f'O seu excesso foi de {excessoPesoPeixe} quilos de peixes, logo a sua multa de excesso será de R${multaExcesso:.2f} reais.')

# Exercício 15 -
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados
# 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# Obs.: Salário Bruto - Descontos = Salário Líquido.
salarioHora = float(input('Digite quanto você ganha por hora:\n'))
horasMes = float(input('Digite quantas horas você trabalha por mês:\n'))
salarioBruto = (salarioHora * horasMes)
ir = 11/100
pagoIr = (salarioBruto * ir)
inss = 8/100
pagoInss = (salarioBruto * inss)
sindicato = 5/100
pagoSindicato = (salarioBruto * sindicato)
descontos = (ir + inss + sindicato)
salarioLiquido = (salarioBruto - descontos)
print(f'O salário bruto é R${salarioBruto:.2f} reais.')
print(f'O valor pago ao INSS é de {pagoInss:.2f} reais.')
print(f'O valor pago ao sindicato é de {pagoSindicato:.2f} reais.')
print(f'O salário liquido é de {salarioLiquido:.2f} reais.')

# Exercício 16 -
# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
import math
tamanho = float(input('Digite em metros quadrados a área a ser pintada:\n'))
coberturaTinta = tamanho / 3
valorLata = 80
quantidadeTinta = math.ceil(coberturaTinta / 18)
valorTotalTinta = (quantidadeTinta * valorLata)
print(f'Para a quantidade de metros quadrados inseridos, você precisará de {quantidadeTinta} latas de tintas e custará {valorTotalTinta:.2f} reais.')

# Exercício 17 -
# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
import math
tamanho = float(input('Digite o tamanho em metros quadrados a ser pintado:\n'))
coberturaTinta = (tamanho / 6)
valorLata18 = 80
valorLata36 = 25
quantidadeTintaLata = math.ceil(coberturaTinta / 18)
valorTotalLata = (quantidadeTintaLata * 80)
quantidadeTintaGalao = math.ceil(coberturaTinta / 3.6)
valorTotalGalao = (quantidadeTintaGalao * 25)

quantidadeTintaLataGalao = math.ceil(coberturaTinta / 18)  # Começamos com a quantidade mínima de latas
sobraTinta = (quantidadeTintaLataGalao * 18) - coberturaTinta  # Calculamos a sobra de tinta com base nas latas
quantidadeTintaGalao += math.ceil(sobraTinta / 3.6)  # Aumentamos a quantidade de galões para cobrir a sobra
valorTotalLataGalao = (quantidadeTintaLataGalao * valorLata18) + (quantidadeTintaGalao * valorLata36)

print(f'A quantidade de latas necessária para pintar a área desejada é de {quantidadeTintaLata} latas e o valor gasto será de R${valorTotalLata:.2f} reais.')
print(f'A quantidade de galões necessária para pintar a área desejada é de {quantidadeTintaGalao} galões e o valor gasto será de R${valorTotalGalao:.2f} reais.')
print(f'O valor total considerando a mistura de latas e galões será de R${valorTotalLataGalao:.2f}.')

# Exercício 18 -
# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
tamanho = float(input('Digite o tamanho do arquivo para download em MB:\n'))
velocidae = float(input('Digite a velocidade de um link de internet em Mbps:\n'))
tempo = (tamanho * 8) / velocidae
print(f'O tempo de donwload do arquivo será de {tempo} segundos')
