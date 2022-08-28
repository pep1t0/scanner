from datetime import datetime
from socket import socket
import sys
import socket
from datetime import datetime

#Define nuestro objetivo - A MEJORAR CON ARGPARSER
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Conversion de hostname a IPv4
else:
    print('Argumentos invalidos')
    print('Sintaxis: python3 scanner.py <ip>')
    
#Banner - A MEJORAR
print('-' * 50)
print('Escaneando objetivo...' + target)
print('Hora de inicio: ' + str(datetime.now()))
print('-' * 50)

try:
    for port in range(1,1024): # A MEJORAR PASANDO PUERTOS POR PARAMETROS
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) # Devuelve el indicador de valor
        if result == 0:
            print("Puerto {} abierto".format(port))
        s.close()
        
except KeyboardInterrupt:
    print('\n[!] Saliendo del programa')
    sys.exit()

except socket.gaierror:
    print('\[!] No se puede hacer la resolucion de nombres')
    sys.exit()

except socket.error:
    print("\n[!] No se puede establecer conexión con el servidor")
    sys.exit()
    
    
      
    
