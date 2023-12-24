import main
import python_files.asciis as asciis
import os

G = '\033[92m'
N = '\033[0m'

def display_system_info():
    print("")
    print("Obteniendo informacion del sistema...")
    import time
    time.sleep(1.3)
    import subprocess
    url = subprocess.getoutput("systeminfo")
    print(url)
    print("\n")
    print(G+" If you desire can save the output in a file pressing S "+N)
    sysdys_input=input ("Press e to return to main menu, press q to exit:  ")
    if sysdys_input == "e":
        os.system("cls")
        asciis.banner()
        main.options()
        main.get_user_input()
    if sysdys_input == "q":
        os.system("exit")
    if sysdys_input == "s":
        with open("systeminfo.txt", "w") as file:
            file.write(url)
            file.close()
            print("File saved!")
            print("file saved as: systeminfo.txt")
            time.sleep(5)
            os.system("cls")
            asciis.banner()
            sysdys_input=input ("Press e to return to main menu, press q to exit:  ")
            if sysdys_input == "e":
                os.system("cls")
                asciis.banner()
                main.options()
                main.get_user_input()
            if sysdys_input == "q":
                os.system("exit")