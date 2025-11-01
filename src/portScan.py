
import socket
from contextlib import closing

import SComm as SC
import banners as B

try:
    import nmap  # type: ignore
except ModuleNotFoundError:  # pragma: no cover - executed only when python-nmap is missing
    nmap = None  # type: ignore

def PortScan():
    SC.clear_console()
    print(B.BANNER_6)
    ip = input(f"\033[0;35m❱\033[0;32m❱\033[0;35m❱\033[0m Ip objective: ")
    ports = input(f"\033[0;35m❱\033[0;32m❱\033[0;35m❱\033[0m ports (format: a-b where a is the starting and b is the last port to try the scan): ")
    
    # Ensure ports are in the correct format
    if '-' in ports:
        start_port, end_port = ports.split('-')
        ports = f"{start_port.strip()}-{end_port.strip()}"
    else:
        print("Invalid port range format. Please use the format a-b.")
        return
    
    if nmap is not None:
        nm = nmap.PortScanner()
        print(f"Scanning {ip} on ports {ports}...")
        nm.scan(ip, ports)

        for host in nm.all_hosts():
            print(f"Host: {host} ({nm[host].hostname()})")
            print(f"State: {nm[host].state()}")
            for proto in nm[host].all_protocols():
                print(f"Protocol: {proto}")
                lport = nm[host][proto].keys()
                for port in lport:
                    print(f"port: {port}\tstate: {nm[host][proto][port]['state']}")
        print("Scan completed.")
    else:
        try:
            start_port, end_port = map(int, ports.split("-"))
        except ValueError:
            print("Invalid port range. Please provide numeric values (e.g., 20-80).")
            return

        print(f"Scanning {ip} on ports {start_port}-{end_port} using fallback scanner...")
        for port in range(start_port, end_port + 1):
            with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
                sock.settimeout(0.5)
                result = sock.connect_ex((ip, port))
                if result == 0:
                    print(f"Port {port}: OPEN")
        print("Fallback scan completed.")

