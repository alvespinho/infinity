lista = []

n1 = int(input ('Digite um número: '))
n2 = int(input ('Digite um número: '))
n3 = int(input ('Digite um número: '))
n4 = int(input ('Digite um número: '))
n5 = int(input ('Digite um número: '))

lista.extend([n1,n2,n3,n4,n5])
def calcular_media():
    media = sum(lista) / len(lista)
    return media


resultado = calcular_media ()
print (f'A lista {lista} tem média {resultado}')
 