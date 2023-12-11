from carrinhofunc import *

### PROMPT DE COMANDO ###
while True:
    print ('\n### CARRINHO DE COMPRAS ###')
    print ('\n1. Inserir Produto')
    print ('2. Remover Produto')
    print ('3. Ver Carrinho de Compras')
    print ('4. Sair')
    
    escolha = input('\n#### DIGITE O Nº DA OPÇÃO DESEJADA ####\n')
    
### ESCOLHA ADD PRODUTO ###
    if escolha == '1':
        produto = input(' Produto: ')
        preco = float(input(' Preço: '))
        un = int(input (' Unidades: '))
        add_produto(produto, preco, un)
        print (F'\n{un} {produto.upper()} foi adicionado ao carrinho!')
        
### ESCOLHA REMOVER PRODUTO ###
    elif escolha == '2':
        produto = input ('Qual produto deseja remover?  ')
        del_produto(produto)
        print (F'\n{produto.upper()} foi removido do carrinho!')
        
### ESCOLHA VER CARRINHO ###
    elif escolha == '3':
        ver_carrinho()
    
### ESCOLHA SAIR ###
    elif escolha == '4':
        break

### ESCOLHA ERRADO ###
    else:
        print ('Ops! Opção inválida. Tente novamente.')
        