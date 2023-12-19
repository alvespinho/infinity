from functools import reduce

### Lista da questão
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

### Números ao quadrado
def aoquadrado(x):
    return x**2

### Números pares
def pares(x):
    return x % 2 == 0

### Soma dos números
def soma(x, y):
    return x + y


### App

aoquadrado_valores = list(map(aoquadrado, numeros))
print("Valores ao quadrado:", aoquadrado_valores)

pares_valores = list(filter(pares, numeros))
print("Números Pares:", pares_valores)

soma_valores = reduce(soma, numeros)
print("Soma total:", soma_valores)