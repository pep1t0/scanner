from datetime import datetime
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
                
    except socket.gaierror:
        print('\[!] No se puede hacer la resolucion de nombres')

    except socket.error:
        print("\n[!] No se puede establecer conexión con el servidor")


#Define nuestro objetivo - A MEJORAR CON ARGPARSER
if len(sys.argv) == 4:
    target = socket.gethostbyname(sys.argv[1]) #Conversion de hostname a IPv4
else:
    print('Argumentos invalidos')
    print('Sintaxis: python3 scanner-thread.py <ip> <start_port> <end_port>')
    sys.exit()
    
#Banner - A MEJORAR
print('-' * 50)
print('Escaneando objetivo...' + target)
print('Puertos:',sys.argv[2], sys.argv[3], sep='  ')
print('Threads:',NUM_WORKERS)
now = datetime.now()
print('Hora de inicio: ' + now.strftime("%d/%m/%Y %H:%M:%S"))
print('-' * 50)

start_time = time.time()
       
try:
    with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_WORKERS) as executor:
            futures = {executor.submit(checkPort, target, port) for port in range(int(sys.argv[2]),int(sys.argv[3]))}
            concurrent.futures.wait(futures)

except KeyboardInterrupt:
    print('[!] Control+C detectado. Finalizando threads...')   
        
end_time = time.time()
now = datetime.now()

print('-' * 50)
print('Hora de finalizacion: ' + now.strftime("%d/%m/%Y %H:%M:%S"))
print('Tiempo transcurrido: %s segundos' %(end_time - start_time))    
print('-' * 50)
    
    
