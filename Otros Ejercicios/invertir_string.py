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
def invierte (string):
    long = len(string)
    invertido = ""
    for x in range(long, 0, -1):
        invertido+=string[x-1]
    print (invertido)

def main():
    pass

if __name__ == '__main__':
    main()
invierte ("Adioscasdrfasdv")