n = 0
lista = []
while n != 5:
    n = int (input ('Digite 5 números de 0 a 10: '))
    lista.append (n)  
pares = [n for n in lista if n % 2 == 0]
print(f'Os números pares são: {pares}')