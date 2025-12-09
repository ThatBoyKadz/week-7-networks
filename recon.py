# recon.py
import socket
import requests

def get_domain_info(domain):
    try:
        print(f"\n=== Recon for: {domain} ===")

        # 1) Resolve domain to IP (DNS lookup)
        ip = socket.gethostbyname(domain)
        print(f"IP Address   : {ip}")

        # 2) Query a public IP-info API (passive OSINT)
        url = f"https://ipapi.co/{ip}/json/"
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            data = response.json()
            print(f"Organisation : {data.get('org', 'Unknown')}")
            print(f"ASN          : {data.get('asn', 'Unknown')}")
            print(f"City         : {data.get('city', 'Unknown')}")
            print(f"Region       : {data.get('region', 'Unknown')}")
            print(f"Country      : {data.get('country_name', 'Unknown')}")
            print(f"IP Version   : {data.get('version', 'Unknown')}")
        else:
            print("Could not fetch public IP data (non-200 response).")

    except socket.gaierror:
        print("DNS lookup failed — check the domain name (e.g., 'python.org').")
    except requests.exceptions.RequestException as e:
        print(f"Request error when contacting IP info API: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    # Example safe public domain. Change this to test other public domains.
    get_domain_info("python.org")
