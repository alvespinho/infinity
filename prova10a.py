#### MODULANDO CÓDIGO PARA REGISTRO DE MATRÍCULA


from prova10b import *

registro = {}

while True:
    print ('\n##### REGISTRO DE MATRÍCULAS #####')
    print ('''\nDigite o número da opção desejada:\n
            [1] Inserir Aluno/a
            [2] Remover Aluno/a
            [3] Atualizar Aluno/a
            [4] Ver Matrículas 
            [5] Sair\n''')
    escolha = input ('    Nº: ')

    # ADD ALUNO
    if escolha == '1':
        matricula = input('Número de Matrícula: ')
        aluno = input('Nome do Aluno/a: ')
        add_aluno(registro, matricula, aluno)
        print(f'\nALUNO/A {aluno.upper()} de MATRÍCULA {matricula} foi registrado com sucesso.')

    # REMOVER ALUNO
    elif escolha == '2':
        matricula = input('Digite o número de matrícula do aluno/a a ser removido: ')
        del_aluno(registro, matricula)
        print(f'\nALUNO de MATRÍCULA {matricula} foi removido com sucesso.')

    # ATUALIZAR ALUNO
    elif escolha == '3':
        matricula = input('Digite o número de matrícula do aluno/a cujo nome será atualizado: ')
        novo_nome = input('Digite o novo nome do aluno/a: ')
        f5_aluno(registro, matricula, novo_nome)
        print(f'\nNome do ALUNO/A com MATRÍCULA {matricula} foi atualizado para {novo_nome}.')

    # VER ALUNO
    elif escolha == '4':
        ver_aluno(registro)

    # SAIR
    elif escolha == '5':
        break

    else:
        print('Ops! Escolha inválida. Tente novamente.')



    
