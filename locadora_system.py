#### SISTEMA DOS FILMES E GÊNEROS 

import json
from random import randint
usuarios = {}

filmes = {
    "Ação": ["", "", ""],
    "Comédia":["", "", ""],
    "Drama": ["", "", ""],    
}

genero = input ('genero: ')
if genero in filmes.keys():
    print(filmes[genero])
    nomeFilme = input('filme: ')
    if nomeFilme in filmes[genero]:
        print (f'filme {nomeFilme} escolhido')


# for _ in range (3):
#     nome = input ('digite seu nome: ')
#     saldo = int (input ('digite o valor inicial que deseja depositar: '))
#     matricula = randint (1000,9999)
#     usuarios [matricula] = {'nome': nome, 'saldo': saldo}

#     with open ('usuarios.json', 'w') as banco:
#         dados = json.dump (usuarios, banco)


# print (dados)


