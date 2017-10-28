# -*- coding: utf-8 -*-
#######SERVICIOS Y SOLUCIONES INFORMATICAS #####
####### PREREQUISITOS, TENER INSTALADO EL CPU LIMIT
####### DESARROLLADO CON PYTHON 3.4
####### PROBADO EN SUSE ENTERPRISE 12 SP 3
####### LICENCIAMIENTO GPL3
####### RECUERDA HACER MENSION DE LOS DESARROLLADORES
####### PUEDES UTILIZARLO LIBREMENTE PERO SIEMPRE COPIA ESTO
####### JULIO CESAR PEREZ BARBOSA
####### SITIO WEB: ssi1.no-ip.org
import os
import sys
import subprocess
#for datos in range(os.system("ls -l")):
#    print (datos, " ", usuario)
x=1
datos=((subprocess.getoutput('ps -e -o pcpu,cpu,args --sort pcpu')).splitlines())
print (datos)
cantidad = len(datos)
print (cantidad)
try:
    m = 1
    for n in datos:
        if m == cantidad:
            print (n)
            division = n.split(' ')
            son=len(division) - 1
            for m in division:
                print (m)
                z = 1
                if z == 1:
                    division2 = m.split('.')
                    cuantos = len(division2)
                    
                    if x == 1:
                        j = division2[0]
                        #  dividir = int(division2) 
                        if int(j) > 67: 
                            we=division[4]
                            # subprocess.call('cpulimit -l 50 ' + division[son])
                            os.system('cpulimit -l 50 ' + division[son])
                        x=2
        m = m +1
except:
    print ('datos')
    os.system('sudo sync && sudo sysctl -w vm.drop_caches=3')