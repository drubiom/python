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
def generar_n_caracteres(num, car):
    sol = ""
    for x in range(0,num):
        sol+=car
    return sol

def main():
    pass

if __name__ == '__main__':
    main()
print(generar_n_caracteres(5, '*'))