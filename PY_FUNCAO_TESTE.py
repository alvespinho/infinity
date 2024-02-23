### FUNÇÕES COM STRING

# def SomaMenor (lista):
#     lista.sort()
#     return lista[0] + lista[1]

# lista = [10, 5, 9, 16, 11]
# print (lista)
# print (SomaMenor(lista))


def FormatarNomeAutor(nome):
    nomes = nome.split (' ')
    nome_formatado = nomes[-1].upper + ','
    for i in range (len(nomes)-1):
        nome_formatado += nomes [i][0].upper() + '. ' 
        
print (input ())
print (FormatarNomeAutor ('Ayrton Senna'))
