import banners
import systemInfo as S_I
import pinger as P
import info as I
import ipInfoGather as IpInfo
import os
from time import sleep

def mainMenu():
    print(banners.BANNER_2)
    print("╭──────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print("│ \033[0;31m𑁍\033[0m \033[0;35m1.\033[0m \033[0;32mDisplay system Info\033[0m")
    print("│ \033[0;31m𑁍\033[0m \033[0;35m2.\033[0m \033[0;32mPING\033[0m")
    print("│ \033[0;31m𑁍\033[0m \033[0;35m3.\033[0m \033[0;32mIp Info Gather\033[0m")
    print("│ \033[0;31m𑁍\033[0m \033[0;35m4.\033[0m \033[0;32mWIP\033[0m")
    print("│ \033[0;31m𑁍\033[0m \033[0;35m5.\033[0m \033[0;32mWIP\033[0m")
    print("│ \033[0;31m𑁍\033[0m \033[0;35mX.\033[0m \033[0;32mINFO\033[0m")
    print("╰─────────────────────────")
    option = input("Selection: ")
    print(option)
    
    if option == "1":
        os.system("cls")
        S_I.SystemInfo()
    elif option == "2":
        os.system("cls")
        P.pingMenu()
    elif option == "3":
        os.system("cls")
        IpInfo.IpInfoGather()
    elif option == "4":
        print("Has elegido: Cuatro")
    elif option == "5":
        print("Has elegido: Cinco")
    elif option == "x" or "X":
        os.system("cls")
        I.show_info()
    else:
        print("Option not Valid, reloading menu.")
        sleep(2)
        os.system("cls")
        mainMenu()

