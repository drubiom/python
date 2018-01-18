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
unidades = {0:'', 1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX'}
decenas = {0:'', 1:'X', 2:'XX', 3:'XXX', 4:'XL', 5:'L', 6:'LX', 7:'LXX', 8:'LXXX', 9:'XC'}
centenas = {0:'', 1:'C', 2:'CC', 3:'CCC', 4:'CD', 5:'D', 6:'DC', 7:'DCC', 8:'DCCC', 9:'XM'}
millares = {0:'', 1:'M', 2:'MM', 3:'MMM'}

num = -1
cont = 0
numeros = []
while num != 0:
    num = int(input ("Introduce numero:"))
    if num > 3500 or num < 0:
        print("Error en el numero.")
    elif num != 0:
        numeros.append(num)
        cont += 1
for x in range (0, cont):
    actual = str(numeros[x])
    leng = len(actual)
    if leng == 1:
        actual = '000' + actual
    elif leng == 2:
        actual = '00' + actual
    elif leng == 3:
        actual = '0' + actual
    rom_u = unidades[int(actual[3])]
    rom_d = decenas[int(actual[2])]
    rom_c = centenas[int(actual[1])]
    rom_m = millares[int(actual[0])]
    romano = rom_m + rom_c + rom_d + rom_u
    print("El número %s en numeros romanos es %s" %(actual, romano))

