### LISTA CARRINHO VAZIA ###
carrinho = []

### FUNÇÃO ADD PRODUTO ###
def add_produto(produto, preco, un):
    carrinho.append({'Produto':produto, 'Preço':preco, 'Unidades':un})
    
### FUNÇÃO REMOVER PRODUTO ###
def del_produto(produto):
    global carrinho
    
    for item in carrinho:
        if item['Produto'] == produto:
            carrinho.remove(item)
            break
        
### FUNÇÃO VER CARRINHO ###
def ver_carrinho():
    total_preco = 0
    print ('\n### CARRINHO DE COMPRAS ####')
    
    for item in carrinho:
        produto = item['Produto']
        preco = item['Preço']
        un = item['Unidades']
        total_preco += preco * un

        print (F'{produto.upper()}|     ${preco:.2f}|   {un}un|')
    print (F'\n ######### TOTAL: ${total_preco:.2f} #########')