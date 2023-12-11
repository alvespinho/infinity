print('''
###### PEDRA, PAPEL & TESOURA #####
    ''')
i = 1
while i !=0:

    jogada = int(input ('''Escolha a jogada\n
                        1 para PEDRA \n
                        2 para PAPEL \n
                        3 para TESOURA \n
                        Digite a opção de jogada: '''))

    import random
    
    def jogar (jogada:int) -> None:
        
        alternativa = random.randint(1,3)
        
        if jogada == alternativa :
            print('Empate!')
        elif jogada == 1 and alternativa == 2:
            print('Você perdeu!! Tente novamente')
        elif jogada == 1 and alternativa == 3:
            print('Você GANHOU, Parabéns!')
            #### Papel ####
        elif jogada == 2 and alternativa == 1:
            print('Você GANHOU, Parabéns!')
        elif jogada == 2 and alternativa == 3:
            print('Você perdeu, Tente novamente')
            ##### Tesoura ####
        elif jogada == 3 and alternativa == 1:
            print('Você perdeu, Tente novamente')
        elif jogada == 3 and alternativa == 2:
            print('Você GANHOU, Parabéns!')
        else:
            print('Opção invalida!')

    jogar(jogada)





