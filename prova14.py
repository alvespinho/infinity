def media():
    alunos = {}

    while True:
        # Nome do aluno
        nome_aluno = input("Insira o nome do aluno (ou 'sair' para finalizar): ")

        # Sair
        if nome_aluno.lower() == 'sair':
            break

        # Lista vazia de alunos
        if nome_aluno not in alunos:
            alunos[nome_aluno] = []

        # Notas dos alunos
        notas = []
        while True:
            nota = input(f"Insira nota de {nome_aluno} (ou '-1' para finalizar): ")
            if nota == "-1":
                break
            try:
                nota = float(nota)
                notas.append(nota)
            except ValueError:
                print("Número inválido. Tente novamente.")

        # Calcular e armazenar media aritmetica
        if notas:
            aritimetica = sum(notas) / len(notas)
            alunos[nome_aluno].append(aritimetica)
            print(f"A média de {nome_aluno}: {aritimetica:.2f}")
        else:
            print(f"Nenhuma nota inserida para {nome_aluno}.")

    # Calcular e imprimir medias
    print("\nNotas de todos alunos: ")
    for estudante, grades in alunos.items():
        if grades:
            aritimetica = sum(grades) / len(grades)
            print(f"{estudante}: {aritimetica:.2f}")
        else:
            print(f"{estudante}: nenhuma nota inserida. ")

    return alunos

# Chamar função
mediafinal = media()
print("Nota dos alunos:", mediafinal)
