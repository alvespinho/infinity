### LISTA "CARRINHO" VAZIA ###
carrinho = []

### OPÇÃO "ADD PRODUTO" ###
def add_produto(produto, preco, und):
    carrinho.append({'Produto': produto, 'Preço': preco, 'Unidades': und})

### OPÇÃO "REMOVER PRODUTO" ###
def del_produto(produto):
    global carrinho 
    
    for item in carrinho:
        if item['Produto'] == produto:
            carrinho.remove(item)
            break
            
### OPÇÃO "VER CARRINHO" ###
def ver_carrinho():
    total_preco = 0
    print("\n### CARRINHO DE COMPRAS ###")
    
    for item in carrinho:
        produto = item['Produto']
        preco = item['Preço']
        und = item['Unidades']
        total_preco += preco * und
        
        print(f"{produto.upper()}|	${preco:.2f}|	{und} un|")
    
    print(f'\n		###### TOTAL: ${total_preco:.2f} #####')

### PROMPT DE COMANDO ###
while True:
    print("\n### CARRINHO DE COMPRAS ###")
    print("\n1. Inserir Produto")
    print("2. Remover Produto")
    print("3. Ver Carrinho")
    print("4. Sair")

    opcao = input("\n### DIGITE O Nº DA OPÇÃO DESEJADA: ###\n")

### PARA ADD PRODUTO ###
    if opcao == '1':
        produto = input("	Produto: ")
        preco = float(input("	Preço: "))
        und = int(input("	Unidades: "))
        add_produto(produto, preco, und)
        print(f"\n{und} {produto.upper()} foi adicionado ao carrinho")

### PARA REMOVER PRODUTO ###             
    elif opcao == '2':
        produto = input("Produto a ser removido: ")
        del_produto(produto)
        print(f"\n{produto.upper()} foi removido do carrinho.")

### PARA VER CARRINHO ###               
    elif opcao == '3':
        ver_carrinho()

### PARA SAIR ###       
    elif opcao == '4':
        break
        
    else:
        print("Ops! Opção inválida. Tente novamente.")

print("Boas compras!")
