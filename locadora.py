from random import randint
from locadorafunc import *

### MENU ###
while True:
    print('\n### MENU LOCADORA ###')
    print('\n1. Inserir Usuário')
    print('2. Remover Usuário')
    print('3. Ver cadastro')
    print('4. Sair')

    escolha = input('\n#### DIGITE O Nº DA OPÇÃO DESEJADA ####\n')

### ESCOLHA ADD USUÁRIO ###
    if escolha == '1':
        user = input(' USUARIO: ')
        matricula = randint(10000, 99999)
        saldo = float(input(' SALDO: '))
        add_user(user, matricula, saldo)
        print(F'\n{user.upper()} de matrícula {matricula} foi adicionado ao cadastro!')

### ESCOLHA REMOVER USUÁRIO ###
    elif escolha == '2':
        user = input('Qual usuário deseja remover?  ')
        del_user(user)

### ESCOLHA VER CADASTROS ###
    elif escolha == '3':
        ver_cadastro()

### ESCOLHA SAIR ###
    elif escolha == '4':
        break

### ESCOLHA ERRADO ###
    else:
        print('Ops! Opção inválida. Tente novamente.')
