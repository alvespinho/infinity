dados = []
soma_idades = 0
usuarios_below_20 = 0
usuarios_above_40 = 0
oldest_usuario = None
oldest_idade = 0
youngest_genero = None
youngest_idade = 100 #### Referência de Idade

for i in range(5):
    usuario = input(f'Digite o nome do Usuário #{i+1}: ')
    idade = int(input(f'Digite a idade do Usuário #{i+1}: '))
    genero = input(f'Digite o gênero do Usuário #{i+1}: ')
    
    soma_idades += idade
    dados.append({'Usuario': usuario, 'Idade': idade, 'Genero': genero})
    
    #### Atualizar valor da pessoa mais velha
    if idade > oldest_idade:
    	oldest_idade = idade 
    	oldest_usuario = usuario
    
    #### Atualizar valor da idade caçula 
    if idade < youngest_idade:
        youngest_idade = idade
        youngest_genero = genero

    #### Conta quantos usuários abaixo de 20 e 		#### acima de 40
    if idade < 20:
        usuarios_below_20 += 1
    elif idade > 40:
        usuarios_above_40 += 1

media_idades = int(soma_idades / len(dados))
print(f'A média de idades é: {media_idades}')

print(f'O usuário mais velho se chama: {oldest_usuario}')

print(f'Número de usuários abaixo de 20 anos: {usuarios_below_20}')

print(f'Número de usuários acima de 40 anos: {usuarios_above_40}')

print(f'O gênero do usuário mais jovem é: {youngest_genero}')
