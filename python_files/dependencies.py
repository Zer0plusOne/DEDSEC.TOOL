import asciis
import subprocess
import time
import os

def is_nmap_installed():
    try:
        subprocess.check_output(["nmap", "--version"])
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False
# ascii banner
asciis.installation()
print(" DEPENDENCIES TO INSTALL")
print("--------------------------------")
print("\n")
print(" 1. NMAP " + (is_nmap_installed() and "(already installed)" or "(not installed)"))
print("\n")
print("--------------------------------")

USER_INPUT = input(" Do you want to install it? (y/n) ").lower()


if USER_INPUT == "n":
    print("Sea consciente que sin las dependencias algunas funciones no estaran disponibles y puede llevar a crasheos de la TOOL")
    print("Exiting the TOOL")
    time.sleep(1.5)
    os.system("exit")

else:
    print('\n installing dependencies...')
    def instalation():
        os.system("apt-get install nmap")
    instalation()