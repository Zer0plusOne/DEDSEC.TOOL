import os

def clear_console():
    if os.name == 'nt':  # 'nt' indica Windows
        os.system('cls')
    else:  # Cualquier otro sistema operativo se asume que es Unix-based (Linux/macOS)
        os.system('clear')
