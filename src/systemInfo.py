import platform
import psutil
import socket
import os
import banners



def SystemInfo():
    print(banners.BANNER_3)
    print(" ")
    print("Informacion del sistema: ")
    print("="*64)
    print("||=================== General Information ===================||")
    print(f"||  [\033[0;34m+\033[0m] Operating System: {platform.system()} {platform.release()}")
    print(f"||  [\033[0;34m+\033[0m] Host Name: {platform.node()}")
    print(f"||  [\033[0;34m+\033[0m] System Verison: {platform.version()}")
    print(f"||  [\033[0;34m+\033[0m] Architecture: {platform.machine()}")
    print(f"||  [\033[0;34m+\033[0m] Processor Core: {platform.processor()}")
    print("||===================== CPU Information =====================||")
    print(f"||  [\033[0;34m+\033[0m] Fisical cores: {psutil.cpu_count(logical=False)} ")
    print(f"||  [\033[0;34m+\033[0m] Total cores: {psutil.cpu_count(logical=True)}")
    print(f"||  [\033[0;34m+\033[0m] Max Hz: {psutil.cpu_freq().max:.2f} MHz")
    print(f"||  [\033[0;34m+\033[0m] Current Hz: {psutil.cpu_freq().current:.2f} MHz")
    print(f"||  [\033[0;34m+\033[0m] CPU Usage: {psutil.cpu_percent(interval=1)}%")
    print("||=================== Memory Information ===================||")
    mem = psutil.virtual_memory()
    print(f"||  [\033[0;34m+\033[0m] Total: {mem.total / (1024 ** 3):.2f} GB")
    print(f"||  [\033[0;34m+\033[0m] Avalible: {mem.available / (1024 ** 3):.2f} GB")
    print(f"||  [\033[0;34m+\033[0m] Usage: {mem.percent}%")
    print(f"||=================== Disk Information ===================||")
    for partition in psutil.disk_partitions():
        print(f" == {partition.device} ({partition.mountpoint})")
        usage = psutil.disk_usage(partition.mountpoint)
        print(f"||  [\033[0;34m+\033[0m] Total: {usage.total / (1024 ** 3):.2f} GB")
        print(f"||  [\033[0;34m+\033[0m] Occupied: {usage.used / (1024 ** 3):.2f} GB ({usage.percent}%)")
        print(f"||  [\033[0;34m+\033[0m] Free: {usage.free / (1024 ** 3):.2f} GB")
    print("||=================== NET Information ===================||")
    info_interfaces = psutil.net_if_addrs()
    for interface, direcciones in info_interfaces.items():
        for direccion in direcciones:
            if direccion.family == socket.AF_INET:  # IPv4
                print(f"||  [\033[0;34m+\033[0m]Interface: {interface}")
                print(f"  ❱❱❱   [\033[0;33mx\033[0m] IPv4: {direccion.address}")
            elif direccion.family == socket.AF_INET6:  # IPv6
                print(f"  ❱❱❱   [\033[0;33mx\033[0m] IPv6: {direccion.address}")
            elif direccion.family == psutil.AF_LINK:  # MAC
                print(f"  ❱❱❱   [\033[0;33mx\033[0m] MAC: {direccion.address}")