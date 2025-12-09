import nmap

def nmap_scan(host, port_range='1-1024'):
    nm = nmap.PortScanner()

    try:
        # -sV = service detection
        nm.scan(host, port_range, arguments='-sV')

        for host in nm.all_hosts():
            print(f"\nHost: {host} ({nm[host].hostname()})")
            print(f"State: {nm[host].state()}")

            for proto in nm[host].all_protocols():
                print(f"\nProtocol: {proto}")

                ports = nm[host][proto].keys()

                for port in sorted(ports):
                    service = nm[host][proto][port]
                    print(
                        f"Port: {port}\t"
                        f"State: {service['state']}\t"
                        f"Service: {service.get('name', 'unknown')} "
                        f"{service.get('version', '')}"
                    )

    except Exception as e:
        print(f"Error: {e}")


# Safe example: Scan localhost ports 1–10
nmap_scan("127.0.0.1", "1-10")
