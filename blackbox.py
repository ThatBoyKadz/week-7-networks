import requests

def black_box_recon(url):
    try:
        # Send an HTTP HEAD request (minimal request)
        response = requests.head(url, timeout=5)

        print("=== Black Box Findings ===")
        print(f"URL: {url}")
        print(f"Status Code: {response.status_code}")
        print(f"Server: {response.headers.get('Server', 'Unknown')}")
        print(f"Content-Type: {response.headers.get('Content-Type', 'Unknown')}")
        print(f"Powered-By: {response.headers.get('X-Powered-By', 'Unknown')}")

        # Simulation of deeper analysis (fake known info for learning)
        known_info = {
            "server": "Apache 2.4 (Simulated)",
            "vulns": "CVE-2021-41773, CVE-2021-42013 (Directory traversal in Apache 2.4)",
            "notes": "If Server header is hidden, use tools like Nmap, WhatWeb, Wappalyzer."
        }

        print("\n=== Simulated Deeper Analysis ===")
        print(f"Guessed Server: {known_info['server']}")
        print(f"Possible Vulnerabilities: {known_info['vulns']}")
        print(f"Notes: {known_info['notes']}")

    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

# Example test target (safe public domain)
black_box_recon("http://python.com")
