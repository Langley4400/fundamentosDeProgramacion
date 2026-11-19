import math


class Figura:
    def area(self):
        return 0


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2


class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2


figuras = [
    Rectangulo(4, 3),
    Circulo(2),
    Triangulo(6, 5)
]

for figura in figuras:
    print(type(figura).__name__, "Area:", round(figura.area(), 2))