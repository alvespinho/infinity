def add_aluno(registro, matricula, aluno): 
    registro[aluno] = {'Matrícula': matricula, 'Aluno': aluno}

def del_aluno(registro, aluno): 
    if aluno in registro:
        del registro[aluno]

def f5_aluno(registro, matricula, novo_nome):
    for matricula_key, aluno_info in registro.items():
        if aluno_info['Matrícula'] == matricula:
            del registro[matricula_key]
            add_aluno(registro, matricula, novo_nome)
            break

def ver_aluno(registro): 
    for aluno, i in registro.items():
        matricula = i['Matrícula']
        print(f'MATRÍCULA: {matricula}, ALUNO: {aluno}')
