lista = []
alunos = int (input ('Quantidade de alunos: '))
for i in range (alunos):
    idades = int(input(F'Idade do aluno {i}: '))
    lista.append(idades)
    
media = sum(lista) / len(lista)
print(f"A média de idade de sua turma é: {media:.2f}")
