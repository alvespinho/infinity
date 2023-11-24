bingo = 7
num = int(input('Adivinhe o número da máquina: '))
tentativas = 1

while num != bingo:
    if num < bingo:
        print('O número é maior. Tente novamente.')
    else:
        print('O número é menor. Tente novamente.')
    
    num = int(input('Adivinhe o número da máquina: '))
    tentativas += 1

print(f'Parabéns! O número é {bingo}. Você acertou em {tentativas} tentativas.')

