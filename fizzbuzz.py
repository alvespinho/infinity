def FizzBuzz (n):

    for i in range (2, n +1):
        if i % 3 == 0 and i % 5 == 0:
            print ("FizzBuzz")
        elif i  % 3 == 0:
            print ("Fizz")
        elif i % 5 == 0:
            print ("Buzz")
        else:
            print (i)

n = int (input ('Digite um número: '))
FizzBuzz (n)