#### CARRINHO DE COMPRAS ####

lista = []
valor = []
total = 0

while True: 
    produto = input ('#### Insira produto (s para sair): ')
    if produto.lower() == "s":
        break
    else:
        preco = float (input(f'#### Insira o valor de {produto}: $'))
        lista.append (produto)
        valor.append (preco)

print ('######### CARRINHO #########')
for produto in lista:
    print ((produto))

for preco in valor:
    total = total + preco

print (f'Seu total é {total}')