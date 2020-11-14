# -*- coding: utf-8 -*-
from triangulo import Triangulo
from collections import OrderedDict

lado1 = int(input("Ingresa el primer lado: \n"))
lado2 = int(input("Ingresa el seguno lado: \n"))
lado3 = int(input("Ingresa el tercer lado: \n"))

obj = Triangulo(lado1, lado2, lado3)
# print obj.get_hallar_altura()

if __name__ == '__main__':
    end_up = False
    mensaje = 'Escribe la opción que deseas'

    # menu = {'a': confirmar, 'b': hallar_perimetro, 'c': hallar_altura, 'd': hallar_area}

    menu = OrderedDict(
        [
            ('a', obj.confirmar),
            ('b', obj.hallar_perimetro),
            ('c', obj.get_hallar_altura),
            ('d', obj.get_hallar_area)
        ]
    )


    while not end_up:
        print('=' * len(mensaje))
        print(mensaje)
        print('=' * len(mensaje))

        for opcion, function in menu.iteritems():
            choice = '{}) {}'.format(opcion, function.__doc__)
            print(choice)

        value_answer = str(raw_input('\nOpción : ').lower())
        end_up = value_answer == 'terminar'

        tarea = menu.get(value_answer,None) # obtengo el el valor de la llave del diccionario
        if tarea:
            print tarea()

    else:
        print("Hemos finalizado nuestra tarea,\nHasta pronto")
