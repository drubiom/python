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
import random

def main():
    pass

if __name__ == '__main__':
    main()
vidas = 7
cont = 0
con_a = 0
con_f = 0
while (vidas > 0):
    sol = random.randint(1,10)
    entrada = int(input ("Introduce número:"))
    if entrada != sol:
        vidas -= 1
        con_f += 1
        print("Vaya, no has adivinado el número. Te quedan %i vidas"%(vidas))

    else:
        vidas += 1
        con_a += 1
        print("Bien! sumas una vida! Te quedan %i vidas"%(vidas))
    cont +=1
if vidas == 0:
    print("Vaya, te has quedado sin intentos! Has hecho un total de %i intentos de los cuales has fallado %i y has acertado %i" %(cont, con_f, con_a))


