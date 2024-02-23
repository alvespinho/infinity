### ACHAR O MAIOR NÚMERO ENTRE 3 ESCOLHIDOS PELO USUÁRIO

num1 = int(input("Insira um Número: "))
num2 = int(input("Insira um Número: "))
num3 = int(input("Insira um Número: "))

while (num1 == num2 == num3):
        print (F"{num1}, {num2} e {num3} são iguais.")
        break

if (num1 > num2 and num1 > num3):
        print (F"O maior número é {num1}")
if (num2 > num1 and num2 > num3):
        print (F"O maior número é {num2}")
if (num3 > num2 and num3 > num1):
        print (F"O maior número é {num3}")        

if (num1 < num2 and num1 < num3):
        print (F"O menor número é {num1}")
if (num2 < num1 and num2 < num3):
        print (F"O menor número é {num2}")
if (num3 < num2 and num3 < num1):
        print (F"O menor número é {num3}")      
          
if (num1 == num2):
        print (F"{num1} é igual a {num2}")
if (num2 == num3):
        print (F"{num2} é igual a {num3}")
if (num3 == num1):
        print (F"{num3} é igual a {num1}") 

