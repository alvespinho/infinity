### CADASTRO VAZIO ###
import json
cadastro = {}

### FUNÇÃO ADD USUÁRIO ###
def add_user(user, matricula, saldo):
    cadastro[matricula]={'USUARIO': user, 'SALDO': saldo}
    with open ('locadora/users.json', 'w') as banco:
        json.dump(cadastro,banco, indent=6)

        
    # banco =  open('locadora/users.json', 'w') 
    # json.dump(cadastro[matricula], banco)

### FUNÇÃO REMOVER USUÁRIO ###

def del_user(user):
    global cadastro

    # Read data from the JSON file
    with open('locadora/users.json', 'r') as banco:
        data = json.load(banco)

    # Find and remove the user from the data
    matricula_to_remove = None
    for matricula, item in data.items():
        if item['USUARIO'] == user:
            matricula_to_remove = matricula
            break

    if matricula_to_remove:
        del data[matricula_to_remove]
        print(f'O usuário {user.upper()} foi removido com sucesso.')
    else:
        print(f'O usuário {user.upper()} não foi encontrado.')

    # Write the updated data back to the JSON file
    with open('locadora/users.json', 'w') as banco:
        json.dump(data, banco)



#### FUNÇÃO VER CADASTRO ###


def ver_cadastro():
    print('\n### LOCADORA ####')

    with open('locadora/users.json', 'r') as banco:
        data = json.load(banco)

        for matricula, item in data.items():
            user = item['USUARIO']
            saldo = item['SALDO']
            print(f'Matricula: {matricula} | User: {user} | Saldo: ${saldo}')
