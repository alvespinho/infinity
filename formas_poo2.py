from math import sqrt

class Forma:
    pass

class Retangulo (Forma):
    def __init__ (self, base, altura):
        self.base = base
        self.altura = altura

    def area (self):
        self.area = (self.base * self.altura)
        return self.area
    
    def perimetro (self):
        self.perimetro = ((self.base + self.altura) * 2) 
        return self.perimetro
    
     
class Circulo (Forma):
    def __init__ (self, raio=float):
        self.raio = raio 
    
    def circunferencia (self):
        self.circunferencia = ((self.raio * 3.1415)**2)
        return self.circunferencia

    def area (self):
        self.area = ((self.raio * self.raio)* 3.1415)
        return self.area  

class Triangulo(Forma):
    def __init__ (self, ladoa=float, ladob=float, ladoc=float):
        self.ladoa = ladoa  
        self.ladob = ladob
        self.ladoc = ladoc
    
    def perimetro (self):
        self.perimetro = (self.ladoa + self.ladob + self.ladoc)
        return self.perimetro
    
    def area (self):
        #### USANDO A FÓRMULA DE HERON        
        self.semiperimetro = (self.ladoa + self.ladob + self.ladoc) / 2
        self.area = sqrt(self.semiperimetro * (self.semiperimetro - self.ladoa) * (self.semiperimetro - self.ladob) * (self.semiperimetro - self.ladoc))
        return self.area

def get_float_input (prompt):
    while True:
        try: 
            user_input = float (input(prompt).replace(',', '.'))
            if user_input == 0:
                print ('\nZERO não é uma medida válida. Tente novamente.')
            else:
                return user_input
        except ValueError:
            print ('\nDados inválidos. Verifique os dados e tente novamente.')