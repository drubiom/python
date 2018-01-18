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

def main():
    pass

if __name__ == '__main__':
    main()
upper = 0
alnum = 0
user_input = input('Escribe la contraseña: ')
for c in user_input:
    if c.isupper():
         upper = 1
    if not c.isalnum():
        alnum = 1

if upper == 0 or len(user_input) < 8 or alnum == 0:
    print ('Contraseña denegada')
else: print('Contraseña aceptada')



