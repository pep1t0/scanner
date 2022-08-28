# from datetime import datetime
from socket import socket
import sys
import socket
import time
import concurrent.futures

NUM_WORKERS = 4

def checkPort(target,port):    
    try:
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
        

    except socket.error:
        print("\n[!] No se puede establecer conexión con el servidor")


#Define nuestro objetivo - A MEJORAR CON ARGPARSER
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Conversion de hostname a IPv4
else:
    print('Argumentos invalidos')
    print('Sintaxis: python3 scanner.py <ip>')
    
#Banner - A MEJORAR
print('-' * 50)
print('Escaneando objetivo...' + target)
start_time = time.time()
print('Hora de inicio: ' + start_time)
print('-' * 50)
       
with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_WORKERS) as executor:
        futures = {executor.submit(checkPort, target, port) for port in range(1,1000)}
        concurrent.futures.wait(futures)
        
end_time = time.time()

print('Hora de finalizacion: ' + end_time)
print('Tiempo transcurrido: %ssecs',(end_time - start_time))    

    
    
