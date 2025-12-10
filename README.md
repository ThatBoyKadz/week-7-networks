# Network Reconnaissance Python Tools Portfolio

This portfolio documents a set of Python scripts developed for basic network reconnaissance, port scanning, and passive OSINT gathering.

---

## 1. Overview

The project contains four scripts designed to perform network information gathering:

1. **blackbox.py** – Retrieves IP and network-related information for a domain using passive OSINT.
2. **nmap_scan.py** – Performs a detailed port scan and service detection using Nmap.
3. **portscan_basic.py** – Simple TCP port scanner using Python sockets.
4. **recon.py** – DNS resolution and passive IP info lookup for domains.

This suite is ideal for educational purposes and safe network reconnaissance exercises.

---

## 2. File Explanations

### 2.1 blackbox.py

**Purpose:** Perform passive OSINT on a domain.

**Key Features:**

* DNS lookup to resolve IP address.
* Queries a public IP info API (`ipapi.co`) for organizational and geolocation information.

**Usage:**

```
python blackbox.py
```


<img width="668" height="228" alt="image" src="https://github.com/user-attachments/assets/41663c27-a7fd-4b24-a83b-c9f68bace1e4" />


---

### 2.2 nmap_scan.py

**Purpose:** Detailed port scanning with service detection.

**Key Features:**

* Uses the Python `nmap` library to interface with Nmap.
* Detects open ports and running services.
* Supports scanning a range of ports and identifies service versions.

**Usage:**

```
python nmap_scan.py
```


---

### 2.3 portscan_basic.py

**Purpose:** Basic TCP port scanning.

**Key Features:**

* Scans a list of ports for a given host using sockets.
* Returns a list of open ports.
* Simple and lightweight for quick checks.

**Usage:**

```
python portscan_basic.py
```

*(Example scans localhost ports 22, 80, 443, 8080)*

<img width="716" height="36" alt="image" src="https://github.com/user-attachments/assets/c5a79e7f-bdb4-4f72-8746-ee7afe66815e" />


---

### 2.4 recon.py

**Purpose:** DNS resolution and passive IP information retrieval.

**Key Features:**

* Resolves domain to IP.
* Queries `ipapi.co` for ASN, organization, and geolocation.
* Handles errors gracefully for invalid domains or API issues.

**Usage:**

```
python recon.py
```



<img width="674" height="225" alt="image" src="https://github.com/user-attachments/assets/fba054f0-b2eb-4ec9-aab9-8ff26e0e9add" />


---

## 3. Workflow Demonstration

1. **Domain Recon:** Use `blackbox.py` or `recon.py` to gather passive OSINT about a domain.
2. **Port Scanning:** Use `portscan_basic.py` for quick TCP checks or `nmap_scan.py` for detailed service detection.
3. **Analysis:** Combine the outputs to build a network profile for safe reconnaissance and testing.



---

## 4. Conclusion

This collection of scripts provides a beginner-friendly toolkit for network reconnaissance:

* Passive OSINT gathering.
* DNS resolution.
* TCP port scanning.
* Nmap-based detailed service detection.

It is suitable for educational purposes, penetration testing labs, and safe network security exercises.

---

*(Add all relevant screenshots where indicated to complete the portfolio.)*
