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
anio = int(input("Introduce el año:"))
if anio>2299 or anio<1583:
    while anio>2299 or anio<1583:
        anio = int(input("Error! introduce año:"))
listaM = [1699, 1899, 2199, 2299]
M = 22
for x in range(0,4):
    if anio <= listaM[x]:
        M = M+x
        break
listaN = [1699, 1799, 1899, 2099, 2199, 2299]
N = 2
for y in range(0,6):
    if anio <= listaN[y]:
        N = N+y
        if N==7:
            N=0
        break
a = anio%19
b = anio%4
c = anio%7
d = (19*a+M)%30
e = (2*b+4*c+6*d+N)%7

if d+e<10:
    dia=d+e+22
    mes='marzo'
else:
    dia=d+e-9
    mes='abril'
    if dia == 26:
        dia = 19
    elif dia==25 and d==28 and e==6 and a>10:
        dia = 18
print('El dia de Pascua corresponde el %i de %s' %(dia, mes))
