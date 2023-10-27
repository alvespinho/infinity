#### USUÁRIO E SENHA COM CONDIÇÃO 

print("Olá, seja bem vindo \nFaça já seu cadastro")

email0 = "dan.alves@gmail.com"
pswrd0 = "123"

email = str(input("EMAIL:\n"))
pswrd = str(input("SENHA: \n"))

while email != email0 or pswrd != pswrd0:
        print ("Login inválido. Tente novamente.")
        email = str(input("EMAIL:\n"))
        pswrd = str(input("SENHA: \n"))
else:
        print("Cadastrado efetuado com sucesso!")     
       