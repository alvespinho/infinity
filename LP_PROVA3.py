speed = float (input("Velocidade: "))
limit = 80
fine = (speed - limit) * 20
if speed > limit:
    print (F"Excesso de velocidade!\nValor da multa: ${fine} reais")