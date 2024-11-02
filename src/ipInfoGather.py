import requests
import socket
import banners
import whois

def IpInfoGather():
    print(banners.BANNER_5)
    ip_address = input("\033[0;35m❱\033[0;32m❱\033[0;35m❱\033[0m Ip objective: ")
    
    gather_ip_info(ip_address)

def gather_ip_info(ip_address):
    # Validate the IP address
    try:
        socket.inet_aton(ip_address)
    except socket.error:
        print("Invalid IP address format.")
        return

    # API endpoint for IPinfo
    ipinfo_url = f"https://ipinfo.io/{ip_address}/json"

    # Gathering data from IPinfo
    try:
        response = requests.get(ipinfo_url)
        ip_info = response.json()

        # Display basic information
        print(f"Information for IP: {ip_address}\n")
        print("╭──────────────────────────────────────────────────────────────────────────────────────────────────────────────")
        print(f"│ [\033[0;34m+\033[0m] IP: {ip_info.get('ip')}")
        print(f"│ [\033[0;34m+\033[0m] Hostname: {socket.gethostbyaddr(ip_address)[0] if socket.gethostbyaddr(ip_address) else 'N/A'}")
        print(f"│ [\033[0;34m+\033[0m] City: {ip_info.get('city', 'N/A')}")
        print(f"│ [\033[0;34m+\033[0m] Region: {ip_info.get('region', 'N/A')}")
        print(f"│ [\033[0;34m+\033[0m] Country: {ip_info.get('country', 'N/A')}")
        print(f"│ [\033[0;34m+\033[0m] Location: {ip_info.get('loc', 'N/A')}")
        print(f"│ [\033[0;34m+\033[0m] Postal: {ip_info.get('postal', 'N/A')}")
        print(f"│ [\033[0;34m+\033[0m] Organization: {ip_info.get('org', 'N/A')}")
        print(f"│ [\033[0;34m+\033[0m] ISP: {ip_info.get('isp', 'N/A')}")
        print(f"╰──────────────────────────────────────────────────────────────────────────────")
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from IPinfo: {e}")

