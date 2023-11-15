import os
import sys
import time
import socket
import random
import threading
import getpass
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
os.system("service tor start")
os.system("clear")
def force_fullscreen():
    if os.name == 'nt':
        from ctypes import windll
        windll.kernel32.SetConsoleWindowInfo(
            sys.stdout.fileno(), True, windll.kernel32.GetConsoleWindow()
        )
def options():
    print (" ?. help ")
    print (" 1. ip_info ")
    print (" 2. portscanner ")
    print (" 3. ping ")
    print (" 4. domain_relations ")
    print (" 5. display_system_info ")
    print ("99. exit")
    print ("\n")
def banner():
	print (G+"""
░ ▒░▓  ░▒ ▒▒ ▓▒░ ▒░   ░  ░ ▒ ░   ░ ░▒ ▒  ░░▓  ░▒▓▒ ▒ ▒  ▒▒   ▓▒█░░ ▓░▒ ▒  ░░ ▒▒░ ▒ 
░ ░ ▒  ░░ ░▒ ▒░░  ░      ░ ░       ░  ▒    ▒ ░░░▒░ ░ ░   ▒   ▒▒ ░  ▒ ░ ░   ░ ▒░  ░ 
  ░ ░   ░ ░░ ░ ░      ░    ░ ░   ░         ▒ ░ ░░░ ░ ░   ░   ▒     ░   ░     ░   ░ 
    ░  ░░  ░          ░          ░ ░       ░     ░           ░  ░    ░        ░    
    ░  ░░  ░          ░          ░ ░       ░     ░           ░  ░    ░        ░\033[0m    
                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~			 			\033[92m
▓█████▄ ▓█████ ▓█████▄   ██████ ▓█████  ▄████▄  
▒██▀ ██▌▓█   ▀ ▒██▀ ██▌▒██    ▒ ▓█   ▀ ▒██▀ ▀█  
░██   █▌▒███   ░██   █▌░ ▓██▄   ▒███   ▒▓█    ▄ 
░▓█▄   ▌▒▓█  ▄ ░▓█▄   ▌  ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒
░▒████▓ ░▒████▒░▒████▓ ▒██████▒▒░▒████▒▒ ▓███▀ ░
 ▒▒▓  ▒ ░░ ▒░ ░ ▒▒▓  ▒ ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░
 ░ ▒  ▒  ░ ░  ░ ░ ▒  ▒ ░ ░▒  ░ ░ ░ ░  ░  ░  ▒   
 ░ ░  ░    ░    ░ ░  ░ ░  ░  ░     ░   ░        
   ░       ░  ░   ░          ░     ░  ░░ ░      
 ░              ░                      ░              
	\033[0m""")
	print (N+"Created By \033[92mZer0plusOne\033[0m On Github\n")

def help():
    print ("""
╔\033[94m███████████████████████████████████████████████████████████████\033[93m╗
║\033[92m                          help                                 \033[93m║
║\033[92m---------------------------------------------------------------\033[93m║
║               ?    :  displays this message                   ║
║               exit :  hacks FBI                               ║
║               ip_info  :  gets ip information                 ║
║               portscanner  :  scan ports                      ║
║               ping  :  makes ping to servers                  ║
║               domain_relations: shows domain relations        ║                               
║               port :  port scan                               ║
║               msf  :	metasploit                              ║
║               sys  :	sytem info                              ║
║               info :  info gather                             ║
║               set  :  setoolkit                               ║
║               insta:  instagram bruteforce                    ║
║               hydra:  use hydra                               ║
║               fb   :  facebook bruteforce                     ║
║               gmail:  gmail bruteforce                        ║
║               cupp :  wordlist maker                          ║
║                                                               ║
║                                                               ║
╚\033[94m███████████████████████████████████████████████████████████████\033[93m╝\033[0?m
	""")          
    help_input=input ("Press e to return to main menu, press q to exit ")
    if help_input == "e":
        os.system("cls")
        banner()
        options()
        get_user_input()
    if help_input == "q":
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
        banner()
        options()
        get_user_input()
    if ipinfo_input == "q":
        os.system("exit")
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
        banner()
        options()
        get_user_input()
    if domrel_input == "q":
        os.system("exit")
def display_system_info():
    print("")
    print("Obteniendo informacion del sistema...")
    import time
    time.sleep(1.3)
    import subprocess
    url = subprocess.getoutput("systeminfo")
    print(url)
    sysdys_input=input ("Press e to return to main menu, press q to exit:  ")
    if sysdys_input == "e":
        os.system("cls")
        banner()
        options()
        get_user_input()
    if sysdys_input == "q":
        os.system("exit")
def get_user_input():

    choice=input("Ingresa un numero para elegir una de las opciones: ")
    if choice == "?":
        help()
    if choice == "1":
        ip_info()
    if choice == "2":
        portscanner()
    if choice == "3":
        ping()
    if choice == "4":
        domain_relations()
    if choice == "5":
        display_system_info()
    if choice == "99":
        exit()
banner()
options()
get_user_input()