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
def main():
    pass

if __name__ == '__main__':
    main()
enc = {'M': 0, 'U': 1, 'R': 2, 'C': 3, 'I': 4, 'E': 5, 'L': 6, 'A': 7, 'G': 8, 'O': 9}
desenc = {'0': 'm', '1': 'u', '2': 'r', '3': 'c', '4': 'i', '5': 'e', '6': 'l', '7': 'a', '8': 'g', '9': 'o'}
opc = int(input("Opcion: (1-Encriptar, 2-Desencriptar)"))
if opc == 1:
    frase = input("Introduce una frase/palabra a encriptar")
    sol = ""
    for x in frase:
        if x.upper() in enc:
            sol += str(enc[x.upper()])
        else:
            sol += x
elif opc == 2:
    frase = input("Introduce una frase/palabra a desencriptar")
    sol = ""
    for x in frase:
        if x.upper() in desenc:
            sol += str(desenc[x.upper()])
        else:
            sol += x

print (sol)