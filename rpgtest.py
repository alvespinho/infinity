### LISTA DE GUILD VAZIA ###
guild = []

### OPÇÃO ADD CHAR ###
def add_char(char, tipo, etnia):
    guild.append({'Char': char, 'Tipo': tipo, 'Etnia': etnia})


    ### Obrigatório ter Tipo: Elfo, Humano, Org, Cyclop ###
    ### pelo menos 2 etnias dentro de cada "tipo" ###
    ### dontpad.com/pooref ###



### OPÇÃO SUB CHAR ###
def del_char(char):
    global guild 
    
    for item in guild:
        if item['Char'] == char:
            guild.remove(item)
            break
            
### OPÇÃO VER GUILD ###
def ver_guild():
    total_tipo = 0
    print("\n### RPG ###")
    
    for item in guild:
        char = item['Char']
        tipo = item['Tipo']
        etnia = item['Etnia']
        
        print(f"{char.upper()}|	{tipo}  |	{etnia}")


### PROMPT DE COMANDO ###
while True:
    print("\n### Crie seu Char: ###")
    print("\n1. Inserir Char")
    print("2. Remover Char")
    print("3. Guild")
    print("4. Sair")

    opcao = input("\n### DIGITE O Nº DA OPÇÃO DESEJADA: ###\n")

### PARA ADD CHAR ###
    if opcao == '1':
        char = input("	Char: ")
        tipo = input("	Tipo: ")
        etnia = input("	Etnia: ")
        add_char(char, tipo, etnia)
        print(f"\n{char.upper()} do tipo {tipo.upper()} foi adicionado a Guild")

### PARA SUB CHAR ###             
    elif opcao == '2':
        char = input("Char a ser removido: ")
        del_char(char)
        print(f"\n{char.upper()} foi removido da Guild.")

### PARA VER GUILD ###               
    elif opcao == '3':
        ver_guild()

### PARA SAIR ###       
    elif opcao == '4':
        break
        
    else:
        print("Ops! Opção inválida. Tente novamente.")

print("Seja bem vindo.")