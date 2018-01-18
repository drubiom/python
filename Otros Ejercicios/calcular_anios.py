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

import time

def main():
    pass

if __name__ == '__main__':
    main()
dia = int(input("Introduce DIA nacimiento:"))
mes = int(input("Introduce MES nacimiento:"))
anio = int(input("Introduce AÑO nacimiento:"))
dia_a = int(time.strftime("%d"))
mes_a = int(time.strftime("%m"))
anio_a = int(time.strftime("%Y"))
if mes < mes_a:
    sol = anio_a-anio
elif mes > mes_a:
    sol = anio_a-anio-1
else:
    if dia < dia_a:
        sol = anio_a-anio
    elif dia > dia_a:
        sol = anio_a-anio-1
    else:
        print("Es tu cumpleaños!!")
        sol = anio_a-anio
print("Tienes %i años"%(sol))