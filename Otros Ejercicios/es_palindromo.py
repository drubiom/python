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
def invierte (string):
    long = len(string)
    invertido = ""
    for x in range(long, 0, -1):
        invertido+=string[x-1]
    return invertido

def main():
    pass

if __name__ == '__main__':
    main()
palabra = input("Introduce palabra:")
palabra = palabra.lower()
palabra_inv = invierte (palabra)
if palabra == palabra_inv:
    print ("Es palíndromo")
else: print ("No es palíndromo")