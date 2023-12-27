import os
import python_files.asciis as asciis
import main
import subprocess

R = '\033[91m'
N = '\033[0m'
G = '\033[92m'

def domain_relations():
    print("")
    print("Ingresa el dominio:")
    domain = input().strip()
    print("Obteniendo IP...")
    import time
    time.sleep(1.3)
    import subprocess
    url = subprocess.getoutput(f"curl -s https://api.hackertarget.com/reverseiplookup/?q={domain}")
    print(url)
    domrel_input=input ("Press e to return to main menu, press q to exit:  ")
    if domrel_input == "e":
        os.system("cls")
        asciis.banner()
        main.options()
        main.get_user_input()
    if domrel_input == "q":
        os.system("exit")

def ip_info():
    print("")
    ip1=input("Ingresa la IP:")
    print("Obteniendo datos correspondientes a la IP...")
    import time
    time.sleep(1.3)
    import subprocess
    url = subprocess.getoutput(f"curl -s http://ip-api.com/{ip1}")
    print(url)
    ipinfo_input=input ("Press e to return to main menu, press q to exit:  ")
    if ipinfo_input == "e":
        os.system("cls")
        asciis.banner()
        main.options()
        main.get_user_input()
    if ipinfo_input == "q":
        os.system("exit")

def ping():
    print("")
    print("Ingresa la IP:")
    ip = input().strip()
    print("Escaneando...")
    import time
    time.sleep(1.3)
    import subprocess
    url = subprocess.getoutput(f"ping {ip}")
    print(url)
    time.sleep(5)

def portscanner():
    print("")
    print("Ingresa la IP:")
    ip = input().strip()
    print("Escaneando...")
    import time
    time.sleep(1.3)
    url = subprocess.getoutput(f"nmap {ip} -p 0-65535")
    print(url)
    time.sleep(5)
    URL_INPUT=input("Deseas ver los puertos abiertos y cerrados separados? (Y/N)")

    if URL_INPUT == "Y" or "y":
        # Obtener solo los puertos abiertos y cerrados
        abiertos = url.split(G+' [open] '+N)[1:]
        cerrados = url.split(R+' [closed] '+N)[1:]

        # Convertir a listas de enteros
        abiertos = [int(puerto.split(' ')[0]) for puerto in abiertos]
        cerrados = [int(puerto.split(' ')[0]) for puerto in cerrados]

        print("\nPuertos abiertos:")
        for puerto in abiertos:
            print(puerto)

        print("\nPuertos cerrados:")
        for puerto in cerrados:
            print(puerto)
    if URL_INPUT == "N" or "n":
        print("Escaneo completado, volviendo al menu principal")
        time.sleep(3)
        os.system("cls")
        asciis.banner()
        main.options()
        main.get_user_input()    