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

def comprueba(user, pc):
    if user == pc:
        return 3
    if user == 1:
        if pc == 2:
            print("El papel cubre a la piedra")
            return 2
        elif pc == 3:
            print('La piedra aplasta las tijeras.')
            return 1
        elif pc == 4:
            print('La piedra aplasta al lagarto')
            return 1
        elif pc == 5:
            print('Spock vaporiza la piedra')
            return 2
    if user == 2:
        if pc == 1:
            print("El papel cubre a la piedra")
            return 1
        elif pc == 3:
            print("Las tijeras cortan el papel")
            return 2
        elif pc == 4:
            print('El lagarto se come el papel')
            return 2
        elif pc == 5:
            print('El papel refuta a Spock')
            return 1
    if user == 3:
        if pc == 1:
            print('La piedra aplasta las tijeras.')
            return 2
        elif pc == 2:
            print("Las tijeras cortan el papel")
            return 1
        elif pc == 4:
            print('Las tijeras decapitan al lagarto')
            return 1
        elif pc == 5:
            print('Spock destroza las tijeras')
            return 2
    if user == 4:
        if pc == 1:
            print('La piedra aplasta al lagarto')
            return 2
        elif pc == 2:
            print('El lagarto se come el papel')
            return 1
        elif pc == 3:
            print('Las tijeras decapitan al lagarto')
            return 2
        elif pc == 5:
            print('El lagarto envenena a Spock')
            return 1
    if user == 5:
        if pc == 1:
            print('Spock vaporiza la piedra')
            return 1
        elif pc == 2:
            print('El papel refuta a Spock')
            return 2
        elif pc == 3:
            print('Spock destroza las tijeras')
            return 1
        elif pc == 4:
            print('El lagarto envenena a Spock')
            return 2

def main():
    pass

if __name__ == '__main__':
    main()
ganador = -1
CONT_USER = 0
CONT_PC = 0
print("AL MEJOR DE 3")
print("--------------")
for x in range(0,3):
    sel = int(input("Selecciona (1-Piedra, 2-Papel, 3-Tijera, 4-Lagarto, 5-Spock)"))
    temp = {1: 'Piedra', 2: 'Papel', 3: 'Tijera', 4: 'Lagarto', 5: 'Spock'}
    sel_pc = random.randint(1,5)
    print ("He sacado %s" %(temp[sel_pc]))
    ganador = comprueba(sel, sel_pc)
    if ganador == 1:
        CONT_USER += 1
        print("Has ganado!")
    elif ganador == 2:
        CONT_PC += 1
        print("He ganado yo!")
    else:
        CONT_USER += 1
        CONT_PC += 1
        print("Empate!!")
    print("--------------")
print("----------------------------------------------")
print("----------------------------------------------")
print("El contador final ha quedado así: TU-%i YO-%i" %(CONT_USER, CONT_PC))
if CONT_USER > CONT_PC:
    print("Has ganado!")
elif CONT_PC > CONT_USER:
    print("He ganado yo!")
else: print("Empate!!")