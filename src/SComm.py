import os
import platform

def clear_console():
    # Utiliza secuencias de escape ANSI en vez de clear/cls para mayor compatibilidad
    if platform.system() == "Windows":
        os.system('cls')  # Comando para limpiar en Windows
    elif os.system("clear") != 0:
        # Secuencia de escape ANSI para limpiar pantalla
        print("\033c", end="")
    else:
        os.system('clear')  # Comando para limpiar en Linux/macOS

# Prueba de la función
clear_console()
