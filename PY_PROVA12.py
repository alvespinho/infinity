### ENCONTRANDO MAIO NÚMERO COM FUNÇÕES

def maior_numero (n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2
    
n1 = float(input('Número 1: '))
n2 = float(input('Número 2: '))


### FUNÇÃO CONDICIONAL
result = maior_numero(n1, n2)
print (f'Aqui, {result} é o maior número.')

### FUNÇÃO BUILT-IN MAX
print (f'E aqui, {max(n1, n2)} também.')
