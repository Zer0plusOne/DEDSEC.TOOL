import main
import python_files.asciis as asciis
import main
import os

N = '\033[0m'
R = '\033[91m'

def info_gather():
    asciis.workingprocess()
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
            asciis.banner()
            main.options()
            main.get_user_input()