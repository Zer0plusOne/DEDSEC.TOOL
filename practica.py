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

def workingprocess():
    print (R+"""
                                        
            ████████████████            
        ████████████████████████        
      ██████████████████████████        
      ████████████████████████████      
    ████████████████████████████████    
  ██      ██      ██        ██      ██  
  ██  ██  ████  ████  ████  ██  ██  ██  
  ██  ████████  ████  ████  ██  ██  ██  
  ██    ██████  ████  ████  ██  ██  ██  
  ████    ████  ████  ████  ██      ██  
  ██████  ████  ████  ████  ██  ██████  
  ██  ██  ████  ████  ████  ██  ██████  
  ██      ████  ████        ██  ██████  
    ████████████████████████████████    
      ████████████████████████████      
      ██████████████████████████        
        ██████████████████████          
            ██████████████████                                                                                           
"""+N)
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
║                                                               ║
║               ?    :  displays this message                   ║
║               exit :  hacks FBI                               ║
║               ip_info  :  gets ip information                 ║
║               portscanner  :  scan ports                      ║
║               ping  :  makes ping to servers                  ║
║               domain_relations: shows domain relations        ║                               
║               port :  port scan                               ║
║               sys  :	sytem info                              ║
║               info :  info gather from a target               ║
║               A_info  :  info gather from a archive           ║
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
def info_gather():
    workingprocess()
    print("THIS IS CURRENTLY UNDER DEVELOPMENT")
    print("Want to see project that can be helpful with that function?")
    info_input=input ("Enter K if you want to or press P to return to main menu:  ")
    if info_input == "k":
        print("\n")
        print("\n")
        print("LIST OF PROJECTS [ GITHUB ]")
        print("--------------------------------------------------------------------")
        print("https://github.com/sherlock-project")
        print("https://github.com/Err0r-ICA/InfoWeb")
        print("https://github.com/trojanx6/user-scan")
        print("https://github.com/KURO-CODE/DoxTracker/blob/master/DoxTracker.py")
        print("https://github.com/wishihab/userrecon")
        print("--------------------------------------------------------------------")
        print("\n")
        print("\n")
        print(R+"THOSE CAN BE USED ILLEGALLY BUT THE AUTHORS ARE NOT RESPONSIBLE FOR THE DAMAGES CAUSED")
        print(R+"AND SO DOES THE AUTHOR OF THIS TOOL"+N)
        print("\n")
        info_input=input ("Enter P to return to main menu:  ")
        if info_input == "p":
            os.system("cls")
            banner()
            options()
            get_user_input()
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
    print("\n")
    print(G+" If you desire can save the output in a file pressing S "+N)
    sysdys_input=input ("Press e to return to main menu, press q to exit:  ")
    if sysdys_input == "e":
        os.system("cls")
        banner()
        options()
        get_user_input()
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
            banner()
            sysdys_input=input ("Press e to return to main menu, press q to exit:  ")
            if sysdys_input == "e":
                os.system("cls")
                banner()
                options()
                get_user_input()
            if sysdys_input == "q":
                os.system("exit")

def meta_info():
    workingprocess()
    print("THIS IS CURRENTLY UNDER DEVELOPMENT")
    print(R+"CURRENTLY THERE ARE NO PROJECTS AVALIBLE FOR THIS FUNCTION"+N)
    print("Please try again later, now entering to main menu")
    time.sleep(5)
    os.system("cls")
    banner()
    options()
    get_user_input()
def get_user_input():

    choice=input("Ingresa un numero para elegir una de las opciones: ")
    if choice == "?":
        os.system("cls")
        help()
    if choice == "1":
        os.system("cls")
        ip_info()
    if choice == "2":
        os.system("cls")
        portscanner()
    if choice == "3":
        os.system("cls")
        ping()
    if choice == "4":
        os.system("cls")
        domain_relations()
    if choice == "5":
        os.system("cls")
        display_system_info()
    if choice == "6":
        os.system("cls")
        info_gather()
    if choice == "7":
        os.system("cls")
        meta_info()
    if choice == "99":
        os.system("cls")
        exit()
banner()
options()
get_user_input()
