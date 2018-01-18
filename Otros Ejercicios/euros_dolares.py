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
import urllib.request
import os

url = 'http://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml'
urllib.request.urlretrieve(url, 'monedas.xml')

archivo = open('monedas.xml','r')
for x in range(0,8):
    linea = archivo.readline()
moneda = archivo.readline()
moneda = moneda[30:36]
print(moneda)

euros = float(input("Introduce Euros:"))
dolares = euros * float(moneda)

print("%.2f Euros son %.2f Dolares" %(euros,dolares))
