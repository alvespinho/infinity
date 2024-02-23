### CALCULANDO MÉDIA DE NÚMEROS ATÉ O USUÁRIO FINALIZAR PROGRAMA COM 0

soma = []
num = int (input('Digite os números para análise (0 finaliza): '))

while num != 0:
    soma.append(num)
    num = int (input('Digite os números para análise (0 finaliza): '))
    contagem = len (soma)
    total = sum(soma)
    media = total / len(soma)
    if num == 0:
        print (f'   A quantidade de números listados: {contagem}')
        print (f'   O valor total dos números listados é: {total}')
        print (f'   A média dos números listados é: {int (media)}')
