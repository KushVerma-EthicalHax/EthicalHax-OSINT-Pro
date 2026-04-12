import tkinter as tk
import requests
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import socket
import random

# ---------------- MATRIX HEADER ---------------- #
def update_matrix():
    chars = "01"
    line = "".join(random.choice(chars) for _ in range(60))
    matrix_label.config(text=line)
    app.after(150, update_matrix)

# ---------------- OUTPUT ---------------- #
def show(text):
    output.config(state="normal")
    output.delete(1.0, tk.END)
    output.insert(tk.END, text)
    output.config(state="disabled")

# ---------------- FUNCTIONS ---------------- #

def username_scan():
    username = entry.get()
    sites = {
        "Instagram": f"https://www.instagram.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Telegram": f"https://t.me/{username}"
    }

    result = "=== USERNAME SCAN ===\n\n"
    for site, url in sites.items():
        try:
            res = requests.get(url, timeout=5)
            if res.status_code == 200:
                result += f"[FOUND] {site}: {url}\n"
            else:
                result += f"[NOT FOUND] {site}\n"
        except:
            result += f"[ERROR] {site}\n"

    show(result)

def email_scan():
    email = entry.get()
    if "@" in email and "." in email:
        domain = email.split("@")[-1]
        show(f"=== EMAIL ===\n\nValid Email\nDomain: {domain}")
    else:
        show("Invalid Email")

def phone_scan():
    number = entry.get()
    try:
        if not number.startswith("+"):
            number = "+91" + number

        parsed = phonenumbers.parse(number)

        result = f"""
=== PHONE INFO ===

Country: {geocoder.description_for_number(parsed, "en")}
Carrier: {carrier.name_for_number(parsed, "en")}
Timezone: {timezone.time_zones_for_number(parsed)}
"""
        show(result)
    except:
        show("Invalid Number")

def ip_scan():
    ip = entry.get()
    try:
        data = requests.get(f"http://ip-api.com/json/{ip}", timeout=5).json()

        result = f"""
=== IP INFO ===

Country: {data.get('country')}
City: {data.get('city')}
ISP: {data.get('isp')}
Latitude: {data.get('lat')}
Longitude: {data.get('lon')}
Map: https://www.google.com/maps?q={data.get('lat')},{data.get('lon')}
"""
        show(result)
    except:
        show("Invalid IP")

def domain_scan():
    domain = entry.get()
    try:
        ip = socket.gethostbyname(domain)
        show(f"=== DOMAIN ===\n\nResolved IP: {ip}")
    except:
        show("Invalid Domain")

def link_scan():
    url = entry.get()
    try:
        res = requests.get(url, timeout=5)
        show(f"=== LINK ===\n\nStatus Code: {res.status_code}")
    except:
        show("Invalid URL")

# 🔥 SCAN ALL
def scan_all():
    data = entry.get()

    result = "=== FULL OSINT SCAN ===\n\n"

    # Username
    sites = ["instagram.com", "github.com", "twitter.com"]
    for s in sites:
        url = f"https://{s}/{data}"
        try:
            if requests.get(url, timeout=5).status_code == 200:
                result += f"[FOUND] {url}\n"
        except:
            pass

    # Email
    if "@" in data:
        result += f"\nEmail Domain: {data.split('@')[-1]}\n"

    # IP
    try:
        ip_data = requests.get(f"http://ip-api.com/json/{data}", timeout=5).json()
        if ip_data.get("country"):
            result += f"\nIP Location: {ip_data.get('city')}, {ip_data.get('country')}\n"
    except:
        pass

    show(result)

# ---------------- GUI ---------------- #

app = tk.Tk()
app.title("ETHICALHAX CYBER TERMINAL 🔥")
app.geometry("600x700")
app.configure(bg="black")

# MATRIX HEADER
matrix_label = tk.Label(app, fg="#00ff00", bg="black", font=("Courier", 8))
matrix_label.pack()
update_matrix()

# TITLE
tk.Label(app, text="ETHICALHAX OSINT PRO", fg="#00ff00", bg="black",
         font=("Courier", 16, "bold")).pack(pady=5)

# INPUT
entry = tk.Entry(app, width=50, bg="black", fg="#00ff00", insertbackground="#00ff00")
entry.pack(pady=10)

# BUTTON STYLE
btn = {
    "bg": "black",
    "fg": "#00ff00",
    "activebackground": "#003300",
    "font": ("Courier", 10),
    "width": 35
}

tk.Button(app, text="Username Scan 🔍", command=username_scan, **btn).pack(pady=3)
tk.Button(app, text="Email Check 📧", command=email_scan, **btn).pack(pady=3)
tk.Button(app, text="Phone Lookup 📱", command=phone_scan, **btn).pack(pady=3)
tk.Button(app, text="IP Tracker 🌐", command=ip_scan, **btn).pack(pady=3)
tk.Button(app, text="Domain Lookup 🌍", command=domain_scan, **btn).pack(pady=3)
tk.Button(app, text="Link Checker 🔗", command=link_scan, **btn).pack(pady=3)
tk.Button(app, text="🔥 Scan All", command=scan_all, **btn).pack(pady=10)

# OUTPUT TERMINAL
output = tk.Text(app, height=20, bg="black", fg="#00ff00")
output.pack(pady=10)
output.config(state="disabled")

app.mainloop()
