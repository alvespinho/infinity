alunos_matriculados = []

def add_aluno(aluno, matricula):
    alunos_matriculados.append({'Aluno': aluno, 'Matrícula': matricula})
    print(f'{aluno.upper()} foi adicionado ao Sistema! Matrícula de número: {matricula}')

def del_aluno(aluno):
    global alunos_matriculados
    for item in alunos_matriculados:
        if item['Aluno'] == aluno:
            alunos_matriculados.remove(item)
            print(f'{aluno.upper()} foi removido do Sistema!')
            break

def ver_alunos():
    print('\n### SISTEMA DE MATRÍCULAS ####')
    for item in alunos_matriculados:
        print(f"{item['Aluno']} | {item['Matrícula']}")

while True:
    print('\n### SISTEMA DE MATRÍCULAS ###')
    print('1. Inserir Aluno')
    print('2. Remover Aluno')
    print('3. Ver Alunos Matriculados')
    print('4. Sair')

    escolha = input('\n#### DIGITE O Nº DA OPÇÃO DESEJADA ####\n')

    if escolha == '1':
        aluno = input('Aluno: ')
        matricula = int(input('Nº de Matrícula: '))
        add_aluno(aluno, matricula)
    elif escolha == '2':
        aluno = input('Qual aluno deseja remover?  ')
        del_aluno(aluno)
    elif escolha == '3':
        ver_alunos()
    elif escolha == '4':
        break
    else:
        print('Ops! Opção inválida. Tente novamente.')
