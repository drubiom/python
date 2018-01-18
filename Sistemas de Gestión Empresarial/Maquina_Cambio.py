#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      david.rubio
#
# Created:     09/01/2018
# Copyright:   (c) david.rubio 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import string
import sys
import os
os.chdir('c:\Python\\archivos')

def consultar(monedas):
    for c in monedas:
        print ("Monedas de %s: %i"%(c,monedas[c]))

def cambio(monedas):
    #ALGORITMO VORAZ
    cantidad = float(input("Introduce la cantidad que quieres obtener"))
    llevo = 0
    debe = cantidad
    devolucion = {'50': 0, '20': 0, '10': 0, '5': 0, '2': 0, '1': 0, '0.50': 0, '0.20': 0, '0.10': 0, '0.05': 0}
    disponibles = [50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10, 0.05]
    for y in range(0,10):
        if y>5:
            temp = ("%.2f"%(disponibles[y]))
        else: temp = ("%i"%(disponibles[y]))
        for x in range(monedas["%s" %(temp)]):
            if cantidad > llevo:
                debe -= disponibles[y]
                llevo += disponibles[y]
                if cantidad >= llevo:
                    devolucion[temp] += 1
                else:
                    debe += disponibles[y]
                    llevo -= disponibles[y]
            elif cantidad == llevo:
                break;
            else: continue
    print (devolucion)
    for c in devolucion:
        if devolucion[c] != 0:
            print ("Monedas de %s: %i"%(c,devolucion[c]))

def reponer(monedas):
    for c in monedas:
        monedas[c] += 20

def guardar(monedas):
    tosave = ""
    for c in monedas:
        tosave += "%s %i\n" %(c, monedas[c])
        fichero = open ( 'monedas.txt', 'w' )
        fichero.write(tosave)
        fichero.close()

def main():
    pass

if __name__ == '__main__':
    main()
monedas = {'50': 50,  '20': 50, '10': 50, '5': 50, '2': 50, '1': 50, '0.50': 50, '0.20': 50, '0.10': 50, '0.05': 50}
fichero = open('monedas.txt')
temp = fichero.readline()
if temp=='':
    monedas = {'50': 50,  '20': 50, '10': 50, '5': 50, '2': 50, '1': 50, '0.50': 50, '0.20': 50, '0.10': 50, '0.05': 50}
else:
    for x in range(0, 10):
        temp2 = temp.split(' ')
        print (temp2)
        monedas[temp2[0]] = int(float(temp2[1]))
        if x<9:
            temp = fichero.readline()
fichero.close()

user_input = 0
while(user_input != '5'):
    print("*******MENÚ*******")
    print("1.-Consultar dinero")
    print("2.-Dar cambio")
    print("3.-Reponer cambio")
    print("4.-Guardar estado")
    user_input = input('Escribe la opción que deseas: ')
    opciones = { '1': consultar, '2': cambio, '3': reponer, '4': guardar}
    if user_input != '5':
        opciones[user_input](monedas)
        input('Pulse una tecla para continuar...')