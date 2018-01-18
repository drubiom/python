#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      david.rubio
#
# Created:     09/01/2018
# Copyright:   (c) david.rubio 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import string

def main():
    pass

if __name__ == '__main__':
    main()
user_input = input('Escribe el dni con la letra: ')
letra = user_input[8]
letra_correcta = "TRWAGMYFPDXBNJZSQVHLCKE"[int(user_input[:-1])%23]
if letra == letra_correcta:
    print ("Correcto")
else: print("Incorrecto")


