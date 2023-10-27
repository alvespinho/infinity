print('#################### Seja bem vindo ao nosso app! ####################')
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
cidade = input('  Digite seu endereço: \nCidade: ')
estado = input('Estado: ')
rua = input('Rua: ')
bairro = input ('Bairro: ')
cep = int(input('Digite seu CEP (somente números): '))


print(f'''   Olá, {nome}, cadastro realizado com sucesso!
       Confira seus dados, por favor:
       Sua idade é {idade} anos.
       Seu endereço é {rua}, {bairro}, {cidade}, {estado}. CEP: {cep}.''')
