import banners
import requests
import SComm as SC


def rel_dom(api_key=None, domain=None):
    
    if api_key is None:
        api_key = input("\033[0;35m❱\033[0;32m❱\033[0;35m❱\033[0m Enter your SecurityTrails API key: ")
    if domain is None:
        domain = input("\033[0;35m❱\033[0;32m❱\033[0;35m❱\033[0m Enter the domain to search for relations: ")

    SC.clear_console()

    url = f"https://api.securitytrails.com/v1/domain/{domain}/associated"
    headers = {
        "APIKEY": api_key
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        data = response.json()
        records = data.get("records", [])

        if records:
            print(banners.BANNER_5)  # Mostrar un banner inicial, si está disponible
            print(f"\nRelations for domain {domain}:\n")
            for relation in records:
                print("Domain:", relation.get("hostname", "N/A"))
                print("Shared IP:", relation.get("ip", "N/A"))
                print("First seen:", relation.get("first_seen", "N/A"))
                print("Last seen:", relation.get("last_seen", "N/A"))
                print("Name Servers:", relation.get("nameserver", "N/A"))
                print("Organization:", relation.get("organization", "N/A"))
                print("Country:", relation.get("country", "N/A"))
                print("Last updated:", relation.get("last_seen", "N/A"))
                print("-" * 50)
        else:
            print(f"No relations found for domain: {domain}")
            
    except requests.exceptions.HTTPError as e:
        print(f"Error getting data from SecurityTrails API: {e}")