### TESTES COM LISTAS

idades = input('Digite as idades dos alunos separadas por espaço: ')
valores = idades.split()

for i in range(len(valores)):
    valores[i] = int(valores[i])

print("A média de idade de sua turma é: ", sum(valores) / len(valores))
