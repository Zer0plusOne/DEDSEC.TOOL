
import nmap
import SComm as SC
import banners as B

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

