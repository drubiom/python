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
dias = int(input("Introduce dias:"))
horas = int(input("Introduce horas:"))
minutos = int(input("Introduce minutos:"))
print("Número total de segundos: %i" %(dias*86400 +horas*3600+minutos*60))