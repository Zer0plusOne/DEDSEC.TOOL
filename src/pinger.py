import os
import subprocess
from scapy.all import IP, ICMP, sr1
import time
from time import sleep
import banners

def realizar_ping(destino, num_pings=10):
    print(f"\nDoing {num_pings} pings to {destino}:\n")
    for i in range(num_pings):
        # Ejecuta el comando ping usando subprocess
        resultado = subprocess.run(
            ["ping", "-c", "1", destino],
            capture_output=True,
            text=True
        )
        
        # Verifica si el ping fue exitoso
        if "1 packets transmitted, 1 received" in resultado.stdout:
            # Extrae y muestra el tiempo de respuesta
            tiempo = resultado.stdout.split("time=")[1].split(" ")[0]
            print(f"Ping {i + 1}: Response in {tiempo} ms")
        else:
            print(f"Ping {i + 1}: No Response")
    print("\nPing completado.\n")

def realizar_traceroute(destino, max_saltos=30):
    print(f"\nDoing traceroute to {destino} with a max of {max_saltos} jumps:\n")
    
    for ttl in range(1, max_saltos + 1):
        # Crea el paquete IP con el TTL específico y el destino
        paquete = IP(dst=destino, ttl=ttl) / ICMP()
        
        # Mide el tiempo de envío y recepción
        inicio = time.time()
        respuesta = sr1(paquete, timeout=2, verbose=0)
        fin = time.time()
        
        # Calcula el tiempo de respuesta
        rtt = (fin - inicio) * 1000  # Convertir a milisegundos
        
        if respuesta is None:
            print(f"{ttl}: * * * (No Response)")
        else:
            # Obtiene la IP de la respuesta y muestra el RTT
            print(f"{ttl}: {respuesta.src} - Response time: {rtt:.2f} ms")
            
            # Si hemos alcanzado el destino, terminamos
            if respuesta.src == destino:
                print("\nTraceroute completed.")
                break
    else:
        print("\nTraceroute finished without arriving to destination.")


def pingMenu():
    print(banners.BANNER_4)
    destino = input("\033[0;35m❱\033[0;32m❱\033[0;35m❱\033[0m Ip objective: ")
    os.system("cls")
    print(banners.BANNER_4)
    while True:
        print("╭──────────────────────────────────────────────────────────────────────────────────────────────────────────────")
        print("│ \033[0;31m𑁍\033[0m \033[0;35m1.\033[0m \033[0;32mPing realization (10 traces)\033[0m")
        print("│ \033[0;31m𑁍\033[0m \033[0;35m2.\033[0m \033[0;32mTraceroute\033[0m")
        print("│ \033[0;31m𑁍\033[0m \033[0;35m3.\033[0m \033[0;32mEXIT\033[0m")
        print("╰──────────────────────────────────────────────────────────────────────────────")

        opcion = input("OPTION: ")
        if opcion == '1':
            realizar_ping(destino)
        elif opcion == '2':
            realizar_traceroute(destino)
        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("No valid option, reloading...")
            sleep(2)
            pingMenu()