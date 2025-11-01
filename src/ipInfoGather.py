import json
import socket
import urllib.error
import urllib.request
from typing import Any, Dict, Optional

import banners
import SComm as SC

try:
    import requests  # type: ignore
except ModuleNotFoundError:  # pragma: no cover - executed only when requests is missing
    requests = None  # type: ignore

try:
    import shodan  # type: ignore
except ModuleNotFoundError:  # pragma: no cover - executed only when shodan is missing
    shodan = None  # type: ignore

try:
    import whois  # type: ignore
except ModuleNotFoundError:  # pragma: no cover - executed only when python-whois is missing
    whois = None  # type: ignore

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

def _http_get_json(url: str, headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Fetch JSON data using requests when available or urllib as a fallback."""

    if requests is not None:
        response = requests.get(url, headers=headers or {}, timeout=10)
        response.raise_for_status()
        return response.json()

    request = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(request, timeout=10) as resp:  # nosec: B310 - controlled URL
        data = resp.read().decode("utf-8")
        return json.loads(data)


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
        ip_info = _http_get_json(ipinfo_url)
        try:
            hostname = socket.gethostbyaddr(ip_address)[0]
        except (socket.herror, socket.gaierror):
            hostname = 'N/A'
        print(f"Information for IP: {ip_address}\n")
        print("╭──────────────────────────────────────────────────────────────────────────────")
        print(f"│ [\033[0;34m+\033[0m] IP: {ip_info.get('ip')}")
        print(f"│ [\033[0;34m+\033[0m] Hostname: {hostname}")
        print(f"│ [\033[0;34m+\033[0m] City: {ip_info.get('city', 'N/A')}")
        print(f"│ [\033[0;34m+\033[0m] Region: {ip_info.get('region', 'N/A')}")
        print(f"│ [\033[0;34m+\033[0m] Country: {ip_info.get('country', 'N/A')}")
        print(f"│ [\033[0;34m+\033[0m] Location: {ip_info.get('loc', 'N/A')}")
        print(f"│ [\033[0;34m+\033[0m] Postal: {ip_info.get('postal', 'N/A')}")
        print(f"│ [\033[0;34m+\033[0m] Organization: {ip_info.get('org', 'N/A')}")
        print(f"╰──────────────────────────────────────────────────────────────────────────────")
    except (urllib.error.URLError, json.JSONDecodeError, Exception) as e:  # noqa: BLE001
        print(f"Error fetching data from IPinfo: {e}")

    # WHOIS lookup
    print("WHOIS Information lookup:")
    if whois is None:
        print("WHOIS module not installed. Skipping WHOIS lookup.")
    else:
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
        except Exception as e:  # noqa: BLE001
            print(f"Error fetching WHOIS data: {e}")

    # Shodan lookup
    print("\nShodan Information:")
    if not shodan_key:
        print("No Shodan API key provided. Skipping Shodan lookup.")
    elif shodan is None:
        print("Shodan module not installed. Skipping Shodan lookup.")
    else:
        try:
            shodan_client = shodan.Shodan(shodan_key)
            shodan_info = shodan_client.host(ip_address)
            print(f"╭──────────────────────────────────────────────────────────────────────────────")
            print(f"│ [\033[0;34m+\033[0m] ISP: {shodan_info.get('isp', 'N/A')}")
            print(f"│ [\033[0;34m+\033[0m] Organization: {shodan_info.get('org', 'N/A')}")
            print(f"│ [\033[0;34m+\033[0m] Open Ports: {shodan_info.get('ports', 'N/A')}")
            print(f"│ [\033[0;34m+\033[0m] Operating System: {shodan_info.get('os', 'N/A')}")
            print(f"╰──────────────────────────────────────────────────────────────────────────────")
        except Exception as e:  # noqa: BLE001
            print(f"Error fetching data from Shodan: {e}")

    # VirusTotal lookup
    print("\nVirusTotal Information:")
    if not virustotal_key:
        print("No VirusTotal API key provided. Skipping VirusTotal lookup.")
    else:
        try:
            headers = {"x-apikey": virustotal_key}
            vt_url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip_address}"
            vt_info = _http_get_json(vt_url, headers=headers)
            last_analysis = vt_info['data']['attributes']['last_analysis_stats']
            print(f"╭──────────────────────────────────────────────────────────────────────────────")
            print(f"│ [\033[0;34m+\033[0m] Harmless: {last_analysis.get('harmless', 'N/A')}")
            print(f"│ [\033[0;34m+\033[0m] Malicious: {last_analysis.get('malicious', 'N/A')}")
            print(f"│ [\033[0;34m+\033[0m] Suspicious: {last_analysis.get('suspicious', 'N/A')}")
            print(f"│ [\033[0;34m+\033[0m] Undetected: {last_analysis.get('undetected', 'N/A')}")
            print(f"╰──────────────────────────────────────────────────────────────────────────────")
        except (urllib.error.URLError, json.JSONDecodeError, Exception) as e:  # noqa: BLE001
            print(f"Error fetching data from VirusTotal: {e}")