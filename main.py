from colorama import Fore, init
import requests
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import socket
import os
import time

init(autoreset=True)

# ------------------ BANNER ------------------ #
def banner():
    print(Fore.RED + r"""
╔══════════════════════════════════════════════════════╗
║   ▄████████  ▄█    █▄     ▄████████    ▄████████     ║
║  ███    ███ ███    ███   ███    ███   ███    ███     ║
║  ███    █▀  ███    ███   ███    ███   ███    █▀      ║
║ ▄███▄▄▄     ███    ███  ▄███▄▄▄▄██▀  ▄███▄▄▄         ║
║▀▀███▀▀▀     ███    ███ ▀▀███▀▀▀▀▀   ▀▀███▀▀▀         ║
║  ███    █▄  ███    ███ ▀███████████   ███    █▄      ║
║  ███    ███ ███    ███   ███    ███   ███    ███     ║
║  ██████████  ▀██████▀    ███    ███   ██████████     ║
║                           ███    ███                ║
╠══════════════════════════════════════════════════════╣
║        ⚡ ETHICALHAX OSINT PRO – SHADOW CORE ⚡       ║
║            >> SYSTEM INITIALIZING... <<             ║
║        >> TRACK • TRACE • ANALYZE • REVEAL <<       ║
╠══════════════════════════════════════════════════════╣
║  Developer : Shyam Verma                            ║
║  Mode      : Stealth Recon                          ║
║  Status    : ACTIVE 🔴                              ║
║  Warning   : Authorized Use Only ⚠️                ║
╚══════════════════════════════════════════════════════╝
""")

# ------------------ LOADING ------------------ #
def loading():
    print(Fore.YELLOW + "\n[+] Processing", end="")
    for _ in range(4):
        print(".", end="", flush=True)
        time.sleep(0.3)
    print("\n")

# ------------------ USERNAME SCAN ------------------ #
def username_scan(username):
    print(Fore.CYAN + "\n[+] Scanning username across platforms...\n")

    sites = {
        "Instagram": f"https://www.instagram.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Telegram": f"https://t.me/{username}"
    }

    found = 0

    for site, url in sites.items():
        try:
            res = requests.get(url, timeout=5)

            if res.status_code == 200:
                print(Fore.GREEN + f"[FOUND] {site}: {url}")
                found += 1
            else:
                print(Fore.RED + f"[NOT FOUND] {site}")

        except:
            print(Fore.YELLOW + f"[ERROR] {site}")

    return found

# ------------------ EMAIL CHECK ------------------ #
def email_scan(email):
    print(Fore.CYAN + "[+] Basic Email Analysis")

    if "@" in email and "." in email:
        domain = email.split("@")[-1]
        print(Fore.GREEN + f"Valid Email Format")
        print(f"Domain: {domain}")
        return 1
    else:
        print(Fore.RED + "Invalid Email Format")
        return 0

# ------------------ PHONE LOOKUP ------------------ #
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def phone_scan(number):
    try:
        # Auto add +91 if user enters without country code
        if not number.startswith("+"):
            number = "+91" + number

        parsed = phonenumbers.parse(number)

        print("Country:", geocoder.description_for_number(parsed, "en"))
        print("Carrier:", carrier.name_for_number(parsed, "en"))
        print("Timezone:", timezone.time_zones_for_number(parsed))

        return 1

    except:
        print("Invalid Number")
        return 0

# ------------------ IP TRACKER ------------------ #
def ip_scan(ip):
    try:
        data = requests.get(f"http://ip-api.com/json/{ip}", timeout=5).json()

        print(Fore.GREEN + f"Country: {data.get('country')}")
        print(f"City: {data.get('city')}")
        print(f"ISP: {data.get('isp')}")
        print(f"Latitude: {data.get('lat')}")
        print(f"Longitude: {data.get('lon')}")
        print(f"Map: https://www.google.com/maps?q={data.get('lat')},{data.get('lon')}")

        return 1

    except:
        print("IP Lookup Failed")
        return 0

# ------------------ DOMAIN LOOKUP ------------------ #
def domain_lookup(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(Fore.GREEN + f"Resolved IP: {ip}")
        return 1
    except:
        print(Fore.RED + "Invalid Domain")
        return 0

# ------------------ LINK CHECK ------------------ #
def link_check(url):
    try:
        res = requests.get(url, timeout=5)
        print(Fore.GREEN + f"Status Code: {res.status_code}")
        return 1
    except:
        print(Fore.RED + "Invalid or Unreachable URL")
        return 0

# ------------------ RISK SYSTEM ------------------ #
def risk_score(score):
    print("\n--- RISK ANALYSIS ---")
    if score <= 2:
        print(Fore.GREEN + "[+] LOW RISK")
    elif score <= 4:
        print(Fore.YELLOW + "[+] MEDIUM RISK")
    else:
        print(Fore.RED + "[+] HIGH RISK")

# ------------------ SCAN ALL ------------------ #
def scan_all():
    username = input("Username: ")
    email = input("Email: ")
    phone = input("Phone (+91): ")
    ip = input("IP: ")
    domain = input("Domain: ")
    link = input("URL: ")

    total = 0

    loading()
    total += username_scan(username)

    loading()
    total += email_scan(email)

    loading()
    total += phone_scan(phone)

    loading()
    total += ip_scan(ip)

    loading()
    total += domain_lookup(domain)

    loading()
    total += link_check(link)

    risk_score(total)

# ------------------ MENU ------------------ #
while True:
    banner()

    print(Fore.CYAN + """
[1] Username Scan 🔍
[2] Email Check 📧
[3] Phone Lookup 📱
[4] IP Tracker 🌐
[5] Domain Lookup 🌍
[6] Link Checker 🔗
[7] Scan All 🔥
[0] Exit
""")

    choice = input("Select option: ")

    if choice == "1":
        username = input("Enter username: ")
        username_scan(username)

    elif choice == "2":
        email = input("Enter email: ")
        score = email_scan(email)
        risk_score(score)

    elif choice == "3":
        num = input("Enter phone (+91): ")
        phone_scan(num)

    elif choice == "4":
        ip = input("Enter IP: ")
        ip_scan(ip)

    elif choice == "5":
        domain = input("Enter domain: ")
        domain_lookup(domain)

    elif choice == "6":
        link = input("Enter URL: ")
        link_check(link)

    elif choice == "7":
        scan_all()

    elif choice == "0":
        print("Exiting...")
        break

    else:
        print(Fore.RED + "Invalid Option")
