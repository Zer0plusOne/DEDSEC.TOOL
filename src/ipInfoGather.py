import requests
import socket
import banners
import shodan
import whois
import SComm as SC

def ApiKeys():
    shodan_key = input("SHODAN API KEY: ")
    virustotal_key = input("VirusTotal API KEY: ")
    SC.clear_console()
    return shodan_key, virustotal_key

def IpInfoGather():
    print(banners.BANNER_5)
    ip_address = input("\033[0;35m❱\033[0;32m❱\033[0;35m❱\033[0m Ip objective: ")
    
    # Solicitar las API keys y pasar al método `gather_ip_info`
    shodan_key, virustotal_key = ApiKeys()
    gather_ip_info(ip_address, shodan_key, virustotal_key)

def gather_ip_info(ip_address, shodan_key, virustotal_key):
    # Validar IP
    try:
        socket.inet_aton(ip_address)
    except socket.error:
        print("Invalid IP address format.")
        return

    # Obtener datos de IPinfo
    ipinfo_url = f"https://ipinfo.io/{ip_address}/json"
    try:
        response = requests.get(ipinfo_url)
        ip_info = response.json()
        print(f"Information for IP: {ip_address}\n")
        print("╭──────────────────────────────────────────────────────────────────────────────")
        print(f"│ [\033[0;34m+\033[0m] IP: {ip_info.get('ip')}")
        print(f"│ [\033[0;34m+\033[0m] Hostname: {socket.gethostbyaddr(ip_address)[0] if socket.gethostbyaddr(ip_address) else 'N/A'}")
        print(f"│ [\033[0;34m+\033[0m] City: {ip_info.get('city', 'N/A')}")
        print(f"│ [\033[0;34m+\033[0m] Region: {ip_info.get('region', 'N/A')}")
        print(f"│ [\033[0;34m+\033[0m] Country: {ip_info.get('country', 'N/A')}")
        print(f"│ [\033[0;34m+\033[0m] Location: {ip_info.get('loc', 'N/A')}")
        print(f"│ [\033[0;34m+\033[0m] Postal: {ip_info.get('postal', 'N/A')}")
        print(f"│ [\033[0;34m+\033[0m] Organization: {ip_info.get('org', 'N/A')}")
        print(f"╰──────────────────────────────────────────────────────────────────────────────")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from IPinfo: {e}")

    # WHOIS lookup
    print("WHOIS Information lookup:")
    try:
        whois_info = whois.whois(ip_address)
        print(f"╭──────────────────────────────────────────────────────────────────────────────")
        print(f"│ [\033[0;34m+\033[0m] Register: {whois_info.registrar}")
        print(f"│ [\033[0;34m+\033[0m] WHOIS Server: {whois_info.whois_server}")
        print(f"│ [\033[0;34m+\033[0m] Creation Date: {whois_info.creation_date}")
        print(f"│ [\033[0;34m+\033[0m] Expiration Date: {whois_info.expiration_date}")
        print(f"│ [\033[0;34m+\033[0m] Updated Date: {whois_info.updated_date}")
        print(f"│ [\033[0;34m+\033[0m] Status: {whois_info.status}")
        print(f"╰──────────────────────────────────────────────────────────────────────────────")
    except Exception as e:
        print(f"Error fetching WHOIS data: {e}")

    # Shodan lookup
    print("\nShodan Information:")
    try:
        shodan_client = shodan.Shodan(shodan_key)
        shodan_info = shodan_client.host(ip_address)
        print(f"╭──────────────────────────────────────────────────────────────────────────────")
        print(f"│ [\033[0;34m+\033[0m] ISP: {shodan_info.get('isp', 'N/A')}")
        print(f"│ [\033[0;34m+\033[0m] Organization: {shodan_info.get('org', 'N/A')}")
        print(f"│ [\033[0;34m+\033[0m] Open Ports: {shodan_info.get('ports', 'N/A')}")
        print(f"│ [\033[0;34m+\033[0m] Operating System: {shodan_info.get('os', 'N/A')}")
        print(f"╰──────────────────────────────────────────────────────────────────────────────")
    except Exception as e:
        print(f"Error fetching data from Shodan: {e}")

    # VirusTotal lookup
    print("\nVirusTotal Information:")
    try:
        headers = {"x-apikey": virustotal_key}
        vt_url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip_address}"
        vt_response = requests.get(vt_url, headers=headers)
        if vt_response.status_code == 200:
            vt_info = vt_response.json()
            last_analysis = vt_info['data']['attributes']['last_analysis_stats']
            print(f"╭──────────────────────────────────────────────────────────────────────────────")
            print(f"│ [\033[0;34m+\033[0m] Harmless: {last_analysis['harmless']}")
            print(f"│ [\033[0;34m+\033[0m] Malicious: {last_analysis['malicious']}")
            print(f"│ [\033[0;34m+\033[0m] Suspicious: {last_analysis['suspicious']}")
            print(f"│ [\033[0;34m+\033[0m] Undetected: {last_analysis['undetected']}")
            print(f"╰──────────────────────────────────────────────────────────────────────────────")
        else:
            print("No data found for this IP in VirusTotal.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from VirusTotal: {e}")