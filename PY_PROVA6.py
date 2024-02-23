#### SOMA ENTRE LISTAS

list1 = input("Insira uma lista de números separados por espaço: ").split()
list2 = input("Insira outra lista de números  separados por espaço: ").split()

list1 = [int(num) for num in list1]
list2 = [int(num) for num in list2]

comum = list(set(list1) & set(list2))
soma_comum = sum(comum)

resultado = (comum, soma_comum)

print(resultado)
