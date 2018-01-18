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
for x in range(0,3):
    num = int(input("Introduce numero:"))
    if num % 2 == 0:
        print("%i Es par" %(num))
    else: print("%i Es impar" %(num))