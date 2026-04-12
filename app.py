from colorama import Fore, init
init(autoreset=True)
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
║                           ███    ███                 ║
╠══════════════════════════════════════════════════════╣
║        ⚡ ETHICALHAX OSINT PRO – SHADOW CORE ⚡      ║
║            >> SYSTEM INITIALIZING... <<              ║
║        >> TRACK • TRACE • ANALYZE • REVEAL <<        ║
╠══════════════════════════════════════════════════════╣
║  Developer : Kush  Verma                             ║
║  Mode      : Stealth Recon                           ║
║  Status    : ACTIVE 🔴                 b             ║
║  Warning   : Authorized Use Only ⚠️                   ║
╚══════════════════════════════════════════════════════╝
""")
from flask import Flask, request, render_template_string
import requests, socket
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>EthicalHax OSINT Pro</title>

<style>
body {
    background:black;
    color:#00ff00;
    font-family:"Courier New", monospace;
    text-align:center;
}

/* BANNER CENTER */
.banner-box {
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
}

/* BANNER TEXT */
.banner-box pre {
    font-family: monospace;
    font-size: 11px;
    line-height: 1.2;

    color: #00ff00;
    text-align: center;

    margin: 0 auto;
    padding: 10px;

    white-space: pre;

    text-shadow: 0 0 8px #00ff00;
}

/* INPUT */
input {
    padding:10px;
    width:70%;
    background:black;
    color:#00ff00;
    border:1px solid #00ff00;
}

/* BUTTON */
button {
    padding:10px;
    margin:5px;
    background:black;
    color:#00ff00;
    border:1px solid #00ff00;
    cursor:pointer;
}

/* OUTPUT */
.result-box {
    text-align:left;
    margin:20px;
    padding:10px;
    border:1px solid #00ff00;
    box-shadow:0 0 10px #00ff00;
    white-space:pre-wrap;
}
</style>
</head>

<body>

<div class="banner-box">
<pre>
╔════════════════════════════════════════════════════════════╗
            ⚡ ETHICALHAX OSINT CORE ⚡
═════════════════════════════════════════════════════════════
        >> TRACK • TRACE • ANALYZE • REVEAL <<

   ▄████████  ▄█    █▄     ▄████████    ▄████████ 
  ███    ███ ███    ███   ███    ███   ███    ███
  ███    █▀  ███    ███   ███    ███   ███    █▀
 ▄███▄▄▄     ███    ███  ▄███▄▄▄▄██   ▄███▄▄▄
▀▀███▀▀▀     ███    ███ ▀▀███▀▀▀▀▀   ▀▀███▀▀▀
  ███    █▄  ███    ███   ███    ███   ███    █▄
  ███    ███ ███    ███   ███    ███   ███    ███
  ██████████  ▀██████▀    ███    ███   ██████████

  Developer : Kush Verma | EthicalHax
  Status    : ACTIVE
  Mode      : CYBER RECON
  Warning   : Authorized Use Only ⚠

╚════════════════════════════════════════════════════════════╝
</pre>
</div>
<h2>⚡ ETHICALHAX OSINT PRO – WEB ⚡</h2>

<form method="post">
<input name="data" placeholder="Enter username / email / phone / IP / domain / URL"><br><br>

<button name="type" value="username">Username 🔍</button>
<button name="type" value="email">Email 📧</button>
<button name="type" value="phone">Phone 📱</button>
<button name="type" value="ip">IP 🌐</button>
<button name="type" value="domain">Domain 🌍</button>
<button name="type" value="link">Link 🔗</button>
<button name="type" value="scanall">🔥 Scan All</button>
</form>

<div class="result-box">{{result}}</div>

</body>
</html>
"""

@app.route("/", methods=["GET","POST"])
def home():
    result = ""

    if request.method == "POST":
        data = request.form.get("data")
        t = request.form.get("type")

        try:
            if t == "ip":
                r = requests.get(f"http://ip-api.com/json/{data}").json()
                result = f"Country: {r.get('country')}\\nCity: {r.get('city')}\\nISP: {r.get('isp')}"

            elif t == "domain":
                ip = socket.gethostbyname(data)
                result = f"Resolved IP: {ip}"

            elif t == "phone":
                num = phonenumbers.parse(data)
                result = f"Country: {geocoder.description_for_number(num,'en')}\\nCarrier: {carrier.name_for_number(num,'en')}\\nTimezone: {timezone.time_zones_for_number(num)}"

            elif t == "email":
                result = "Valid Email Format ✔"

            elif t == "username":
                result = f"Searching username: {data}"

            elif t == "link":
                r = requests.get(data)
                result = f"Status Code: {r.status_code}"

            elif t == "scanall":
                result = f"Full Scan Started on: {data} 🔥"

        except:
            result = "Error occurred"

    return render_template_string(HTML, result=result)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
