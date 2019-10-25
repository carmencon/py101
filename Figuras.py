from Punto import *

from math import pi

class Figura:
    def __init__(self, p1,p2):
        self.origen = p1
        self.destino = p2
        self.area = 0
        self.perimetro = 0
    

class Cuadrado (Figura):

     def calcular_area(self):
         lado = self.origen.calcular_distancia(self.destino)
         self.area = lado * lado

     def calcular_perimetro(self):
         lado = self.origen.calcular_distancia(self.destino)
         self.perimetro = lado * 4


class Circulo(Figura):

    def calcular_area(self):
         radio = self.origen.calcular_distancia(self.destino)
         self.area = pi * (radio **2)

    def calcular_perimetro(self):
         radio = self.origen.calcular_distancia(self.destino)
         self.perimetro = (radio *2)


class Rectangulo(Figura):

    def calcular_area(self):
        temp = Punto(self.origen.x,self.destino.y)
        b = temp.calcular_distancia(self.destino)
        a = temp.calcular_distancia(self.origen)
        self.area = (b * a)


    def calcular_perimetro(self):
        temp = Punto(self.origen.x,self.destino.y)
        b = temp.calcular_distancia(self.destino)
        a = temp.calcular_distancia(self.origen)
        self.perimetro = ((b+a)* 2)


class Triangulo(Figura):

    def calcular_area(self):
        temp = Punto(self.origen.x,self.destino.y)
        b = temp.calcular_distancia(self.destino)
        a = temp.calcular_distancia(self.origen)
        self.area = (b * a)/2

