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
def is_vocal (letra):
    vocales = ['a','e','i','o','u','A','E','I','O','U']
    for x in vocales:
        if letra == x:
            return True
    return False

def main():
    pass

if __name__ == '__main__':
    main()
palabra = input ("Escribe una palabra:")
for x in palabra:
    if is_vocal(x):
        print("La primera vocal es %s" %(x))
        break

