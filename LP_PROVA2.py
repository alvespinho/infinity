##### NÚMEROS PARES DADO UMA CONDIÇÃO 

even=[]

for i in range (5):
	numero = int (input ('Digite um número de 0 a 10: '))
	if (numero % 2 ==0):
			even.append(numero)
		
	if numero > 10 or numero < 0:
		print(F'Número inválido. Tente outra vez.')

		break
		
print(F'{even} são números pares.')