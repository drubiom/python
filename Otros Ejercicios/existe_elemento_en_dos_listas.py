#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      david.rubio
#
# Created:     10/01/2018
# Copyright:   (c) david.rubio 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import string
def superposicion(lista1, lista2):
    for x in lista1:
        for y in lista2:
            if x == y:
                return True

    return False

def main():
    pass

if __name__ == '__main__':
    main()
lista1 = ['Hola', 'Avion']
lista2 = ['Barco', 'Avion']
print(superposicion(lista1, lista2))