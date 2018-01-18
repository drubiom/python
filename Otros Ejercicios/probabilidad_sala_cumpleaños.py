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
prob = 0.0
personas = 0
num = int(input("Número de casos:"))
for x in range(0,num):
    bandera = 0
    lista_personas = []
    while (bandera!=1):
        persona = random.randint(1,365)
        for x in lista_personas:
            if x == persona:
                bandera = 1
        lista_personas.append(persona)
    print("Número de personas en la sala: %i" %(len(lista_personas)))
    probact = float(1/len(lista_personas)*100)
    print("Probabilidad actual: %.2f" %(probact))
    prob += probact
    personas += len(lista_personas)
    print("------------------------")
print("------------------------")
print("Probabilidad total: %.2f" %(prob/num))
print("Personas medias en la sala: %.2f" %(float(personas/num)))


