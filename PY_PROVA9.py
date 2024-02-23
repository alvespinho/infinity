### ENCONTRAR MÉDIA DE ALUNO E VERIFICAR SE PASSOU DE ANO COM FUNÇÕES

def verificar(media):
    if media == 10:
        return (f"Parabéns, sua média é 10")
    elif media < 7: 
        return (f"Reprovado")
    elif media >= 7: 
        return (f"Parabéns, você está aprovado!")


def calcular(nota1, nota2, nota3, nota4, nota5):
    return (nota1 + nota2 + nota3 + nota4 + nota5)/ 5
    

#### APP

nota1 = float (input('Digite Nota 1: '))
nota2 = float (input('Digite Nota 2: '))
nota3 = float (input('Digite Nota 3: '))
nota4 = float (input('Digite Nota 4: '))
nota5 = float (input('Digite Nota 5: '))
media = calcular(nota1, nota2, nota3, nota4, nota5)

situacao = verificar(media)
print(media)
print(situacao)






