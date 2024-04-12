'''
Ping script to test if several given hosts (from 1 to 255) in a Class C private network are reachable or not

hostname = your class c net
a = begining of the hosts we look for
b = end of the hosts we look for

If we want to ping the hosts between 192.168.0.10 and 192.168.0.20:
hostname('192.168.0.'), a(10), b(21)

diegoHERNANDO#2021
www.diegohernando.es
'''

import os
import platform

activas = [] # create a list with the reachable IPs
caidas = [] # create a list with the unreachable IPs
    
def pingTo(hostname, a = 1, b = 256): # defaults for beggining and end of the IPs to look for
    
    if platform.system().lower() == "windows":
        for i in range(a, b):
            respuesta = os.system("ping " + hostname + str(i) + " -n 1")
    else:
        for i in range(a, b):
            respuesta = os.system("ping -c 1 " + hostname + str(i))
            activa = False
            if respuesta == 0:
                activa = True
                global activas
                activas.append(hostname + str(i))
            else:
                activa = False
                global caidas
                caidas.append(hostname + str(i))
    
    return activas, caidas


pingTo('192.168.0.', 10, 21)
print('\n\n'+'='*33,'\n')
print('Reachable hosts:', len(activas), '\n', activas)
print('\nUnreachable hosts:', len(caidas), '\n', caidas)
