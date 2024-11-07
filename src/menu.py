import banners
import systemInfo as S_I
import pinger as P
import info as I
import RelDom as RD
import ipInfoGather as IpInfo
import portScan as PC
from time import sleep

import SComm as SC

def mainMenu():
    print(banners.BANNER_2)
    print("╭──────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print("│ \033[0;31m𑁍\033[0m \033[0;35m1.\033[0m \033[0;32mDisplay system Info\033[0m")
    print("│ \033[0;31m𑁍\033[0m \033[0;35m2.\033[0m \033[0;32mPING\033[0m")
    print("│ \033[0;31m𑁍\033[0m \033[0;35m3.\033[0m \033[0;32mIp Info Gather\033[0m")
    print("│ \033[0;31m𑁍\033[0m \033[0;35m4.\033[0m \033[0;32mPort Scanner\033[0m")
    print("│ \033[0;31m𑁍\033[0m \033[0;35m5.\033[0m \033[0;32mRelation Between Domains\033[0m")
    print("│ \033[0;31m𑁍\033[0m \033[0;35mX.\033[0m \033[0;32mINFO\033[0m")
    print("╰─────────────────────────")
    option = input("Selection: ")
    print(option)
    
    if option == "1":
        SC.clear_console
        S_I.SystemInfo()
    elif option == "2":
        SC.clear_console
        P.pingMenu()
    elif option == "3":
        SC.clear_console
        IpInfo.IpInfoGather()
    elif option == "4":
        SC.clear_console
        PC.PortScan()
    elif option == "5":
        SC.clear_console
        RD.rel_dom()
    elif option == "x" or "X":
        SC.clear_console
        I.show_info()
    else:
        print("Option not Valid, reloading menu.")
        sleep(2)
        SC.clear_console()
        mainMenu()

