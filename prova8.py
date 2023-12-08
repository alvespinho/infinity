pessoas = {
    "João": 23,
    "Maria": 28,
    "Pedro": 35,
    "Lucas": 19
}

# Acessar e armazenar a idade de João:
idade_joao = pessoas['João']

# Adicionar Ana, de idade 31:
pessoas["Ana"] = 31

# Função da maior idade:
def maior_idade(dicionario):
    if not dicionario:
        return None
    mais_velho = max(dicionario, key=dicionario.get)
    return mais_velho

# Nome da pessoa mais velha:
mais_velho_nome = maior_idade(pessoas)
print(f"A pessoa mais velha é {mais_velho_nome}.")