#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      david.rubio
#
# Created:     11/01/2018
# Copyright:   (c) david.rubio 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
sumatorio = 0
contador = 0
entrada = int(input("Introduce numero (-1 para terminar):"))
max = 0
min = entrada
while entrada != -1:
    if entrada != -1:
        contador +=1
        sumatorio += entrada
        if entrada > max: max = entrada
        if entrada < min: min = entrada
        entrada = int(input("Introduce numero (-1 para terminar):"))
print("Media: %.2f"%(sumatorio/contador))
print("Máximo: %i"%(max))
print("Mínimo: %i"%(min))