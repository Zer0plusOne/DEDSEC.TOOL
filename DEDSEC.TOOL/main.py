import os
import sys
import time
import socket
import random
import threading
import getpass
import python_files.asciis as asciis
import python_files.help as help
import python_files.net_func as net_func
import python_files.local_func as local_func
import python_files.archives_func as archives_func
import python_files.osint as osint

r = '\033[31m'
W = '\033[90m'
R = '\033[91m'
N = '\033[0m'
G = '\033[92m'
B = '\033[94m'
Y = '\033[93m'
LB = '\033[1;36m'
P = '\033[95m'
Bl = '\033[30m'
O = '\033[33m'
p = '\033[35m'

os.system("cls")
def options():
    print (" ?. help ")
    print (" 1. ip_info ")
    print (" 2. portscanner ")
    print (" 3. ping ")
    print (" 4. domain_relations ")
    print (" 5. display_system_info ")
    print (" 6. info_gather ")
    print (" 7. A_info ")
    print ("99. exit")
    print ("\n")

def get_user_input():

    choice=input("Ingresa un numero para elegir una de las opciones: ")
    if choice == "?":
        os.system("cls")
        help.help()
    if choice == "1":
        os.system("cls")
        net_func.ip_info()
    if choice == "2":
        os.system("cls")
        net_func.portscanner()
    if choice == "3":
        os.system("cls")
        net_func.ping()
    if choice == "4":
        os.system("cls")
        net_func.domain_relations()
    if choice == "5":
        os.system("cls")
        local_func.display_system_info()
    if choice == "6":
        os.system("cls")
        osint.info_gather()
    if choice == "7":
        os.system("cls")
        archives_func.meta_info()
    if choice == "99":
        os.system("cls")
        exit()
    if choice == "":
        print("BLANK PARAM. PLEASE FIX.")
        time.sleep(2)
        get_user_input()

asciis.banner()
options()
get_user_input()

