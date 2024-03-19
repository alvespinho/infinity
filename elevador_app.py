import random

class Elevador:
    def __init__(self, capacidadeTotal, quantidadeAtual, andarTotal, andarAtual):
        self.capacidadeTotal = capacidadeTotal
        self.quantidadeAtual = quantidadeAtual
        self.andarTotal = andarTotal
        self.andarAtual = andarAtual

    def __str__(self):
        return f'''----------------------
Capacidade Total: {self.capacidadeTotal}
Quantidade Atual: {self.quantidadeAtual}
Total de Andares: {self.andarTotal}
Andar Atual: {self.andarAtual}
------------------------ '''

    def subir(self):
        if self.andarAtual < self.andarTotal:
            self.andarAtual += 1
            print('Subindo para o andar:', self.andarAtual)
            self.checar_direcao()
            self.upar_capacidade()
            self.usuarios()
        else:
            print ('O elevador já está no último andar.') 
            print ('Você está no andar mais alto!')

    def descer(self):
        if self.andarAtual > 0:
            self.andarAtual -= 1
            print('Descendo para o andar:', self.andarAtual)
            self.checar_direcao()
            self.upar_capacidade()
            self.usuarios()
        else:
            print ('O elevador já está no térreo.')
            print ('Você já está no térreo!')

    def entrar(self, num_pessoas):
        if self.quantidadeAtual + num_pessoas <= self.capacidadeTotal:
            self.quantidadeAtual += num_pessoas
            print(f'{num_pessoas} pessoa(s) entrou/entraram no elevador.')
        else:
            print ('Capacidade máxima do elevador atingida. Não é possível entrar mais pessoas.')
            print ('O elevador está cheio.')

    def sair(self, num_pessoas):
        if self.quantidadeAtual - num_pessoas >= 0:
            self.quantidadeAtual -= num_pessoas
            print(f'{num_pessoas} pessoa(s) saiu/saíram do elevador.')
        else:
            print ('Não há pessoas suficientes no elevador para sair.')
            print ('Não tem ninguém!')

    def checar_direcao(self):
        if self.andarAtual < self.destino:
            print('Indo para cima.')
        elif self.andarAtual > self.destino:
            print('Indo para baixo.')
        else:
            print('Chegou ao destino.')
            exit()  ### CHEGOU AO DESTINO, PÁRA.

    def upar_capacidade(self):
        if self.quantidadeAtual > 0:
            print(f'{self.quantidadeAtual} pessoa(s) no elevador.')
        else:
            print('O elevador está vazio.')

    def usuarios(self):
        entradas = random.randint(0, self.capacidadeTotal - self.quantidadeAtual)
        saidas = random.randint(0, self.quantidadeAtual)
        if entradas > 0:
            self.entrar(entradas)
        if saidas > 0:
            self.sair(saidas)

    def ir_para_andar(self, destino):
        self.destino = destino
        if self.destino > self.andarAtual:
            print(f'Indo para o andar {self.destino}.')
        elif self.destino < self.andarAtual:
            print(f'Indo para o andar {self.destino}.')
        else:
            print('Você já está neste andar.')
        while self.andarAtual != self.destino:
            if self.destino > self.andarAtual:
                self.subir()
            else:
                self.descer()

# STATUS ALEATÓRIO DO ELEVADOR 
                
andar_inicial = random.randint(0, 5)    # ANDAR INICIAL ALEATÓRIO
pessoas = random.randint(0, 10)         # PESSOAS ALEATÓRIAS ENTRANDO/SAINDO

elevador = Elevador(capacidadeTotal=10, quantidadeAtual=pessoas, andarTotal=5, andarAtual=andar_inicial)

print('\nINFINITY ELEVATOR: ')
print(elevador)

while True:
    try:
        destino = int(input('Digite o andar para onde deseja ir: '))
        
        if destino < 0 or destino > elevador.andarTotal:
            raise ValueError('Andar de destino fora do intervalo permitido.')
        
        elevador.ir_para_andar(destino)
        break
    except ValueError as e:
        print(f'Erro: {e}')
