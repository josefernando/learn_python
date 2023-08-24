import math

class Circulo():
    def __init__(self,raio):
        self.raio = raio
    def circunferencia(self):
        return round((2 * math.pi * self.raio),2)
    def area(self):
        return round((math.pi * self.raio ** 2),2)
    
class Cilindro(Circulo):
    def __init__(self, raio, altura):
        super().__init__(raio)
        self.altura = altura

    def volume(self):
        return self.area() * self.altura  

circulo = Circulo(5)
cilindro = Cilindro(2,5)

circunferencia = circulo.circunferencia()

area = circulo.area()

volume = cilindro.volume()

print(f"Circunferência {circunferencia}")

print(f"Área do círculo {area}")

print(f"Volume {volume}")