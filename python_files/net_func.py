import os
import python_files.asciis as asciis
import main

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
    print("Ingresa el puerto:")
    port = input().strip()
    print("Escaneando...")
    import time
    time.sleep(1.3)
    import subprocess
    url = subprocess.getoutput(f"nmap {ip} -p {port}")
    print(url)
    