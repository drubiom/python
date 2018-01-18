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
sol = random.randint(1,100)
dif = int(input("Introduce dificultad (1-Fácil, 2-Medio, 3-Difícil):"))
if dif == 1:
    intentos = 20
elif dif == 2:
    intentos = 10
else: intentos = 5
entrada = -1
while (entrada != sol and intentos > 0):
    intentos -= 1
    entrada = int(input ("Introduce número:"))
    if entrada>sol:
        print("Es menor")
        print("Te quedan %i intentos"%(intentos))
    elif entrada<sol:
        print("Es mayor")
        print("Te quedan %i intentos"%(intentos))
    else: print("Enhorabuena! Lo has conseguido")
if entrada != sol and intentos == 0:
    print("Vaya, te has quedado sin intentos! Otra vez será")


