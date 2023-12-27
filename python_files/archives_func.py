import python_files.asciis as asciis
import time
import os
import main

N = '\033[0m'
R = '\033[91m'


def meta_info():
    asciis.workingprocess()
    print("THIS IS CURRENTLY UNDER DEVELOPMENT")
    print(R+"CURRENTLY THERE ARE NO PROJECTS AVALIBLE FOR THIS FUNCTION"+N)
    print("Please try again later, now entering to main menu")
    time.sleep(5)
    os.system("clear")
    os.system("clear")
    asciis.banner()
    main.options()
    main.get_user_input()