import main
import python_files.asciis as asciis
import os

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
        asciis.banner()
        main.options()
        main.get_user_input()
    if help_input == "q":
        os.system("exit")  