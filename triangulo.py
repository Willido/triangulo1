# -*- coding: utf-8 -*-
import math # Esto es una funcion para llamar al operador raiz cuadrada
class Triangulo:
    def __init__(self, lado1 = 8, lado2 = 5, lado3 = 3):
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3
    def confirmar(self):
        """Confirmar si es un triangulo"""
        if (self.__lado1 + self.__lado2) > self.__lado3:
            if (self.__lado1 + self.__lado3) > self.__lado2:
                if (self.__lado2 + self.__lado3) > self.__lado1:
                    return "Es un triangulo"
                else:
                    return "No es un triangulo"
            else:
                return "No es un triangulo"
        else:
            return "No es un triangulo"

    def hallar_perimetro(self):
        """Hallar Perímetro"""
        if self.confirmar() == "Es un triangulo":
            return (self.__lado1 + self.__lado2 + self.__lado3)
        else:
            return "No es un triangulo"


    def __hallar_sp(self):
        if self.confirmar() == "Es un triangulo":
            return self.hallar_perimetro()/2.0
        else:
            return "No es un triangulo"

    def get_hallar_altura(self):
        """Hallar Altura"""
        if self.__hallar_sp() > 0:
            return (2.0 / self.__lado3) * (math.sqrt(self.__hallar_sp() * (self.__hallar_sp() - self.__lado1) * (self.__hallar_sp() - self.__lado2) * (self.__hallar_sp() - self.__lado3)))
        else:
            return "No es un triangulo"

    def get_hallar_area(self):
        """Hallar Área"""
        if self.__hallar_sp() > 0:
            return math.sqrt(self.__hallar_sp() * (self.__hallar_sp() - self.__lado1) * (self.__hallar_sp() - self.__lado2) * (self.__hallar_sp() - self.__lado3))
        else:
            return "No es un triangulo"
