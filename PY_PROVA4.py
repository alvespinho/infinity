list1 = (input('Insira uma lista de números separados por espaço e aperte enter: ').split(' '))
list2 = ((input('Insira uma lista de números separados por espaço e aperte enter: ').split(' ')))
list1.extend(list2)
print(list1)


#### OUTRO JEITO POSSÍVEL ###

# list1 = (input('Insira uma lista de números separados por espaço e aperte enter: ').split(' '))
# list2 = ((input('Insira uma lista de números separados por espaço e aperte enter: ').split(' ')))
# for i in list2:
#     list1.append(i)
# print (list1)
