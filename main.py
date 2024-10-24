import certstream
import json
import requests
import whois
import socket
import re
from flask import Flask, render_template

# Kreiraj Flask aplikaciju
app = Flask(__name__)

# Prilagođena lista ključnih reči za BiH
keywords = [
    r"\bbosnia\b", r"\bbosna\b", r"\bposta\b", r"\bposta-ba\b", r"\bposta\.ba\b",
    r"\bedu\.ba\b", r"\bbhposta\b", r"\bbh\b", r"\bposta\.ba\b", r"\bmup\b"
]

# Lista reči za isključivanje
exclude_keywords = ["premierleague", "webapp", "faspro", "greenbackco"]

# Funkcija za proveru DNS-a
def check_dns(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return f"DNS OK, IP: {ip_address}"
    except socket.gaierror:
        return "DNS NOT FOUND"

# Funkcija za proveru WHOIS informacija
def check_whois(domain):
    try:
        w = whois.whois(domain)
        registrar = w.registrar if w.registrar else "N/A"
        creation_date = w.creation_date if w.creation_date else "N/A"
        return f"Registered by: {registrar}, Created on: {creation_date}"
    except Exception as e:
        return f"WHOIS INFO NOT FOUND: {e}"

# Funkcija za proveru HTTP statusa
def check_http_status(domain):
    try:
        response = requests.get(f"http://{domain}", timeout=5)
        return f"HTTP Status: {response.status_code}"
    except requests.ConnectionError:
        return "No HTTP Response"
    except Exception as e:
        return f"HTTP ERROR: {e}"

# Funkcija koja se poziva kada certstream dobije novi događaj
def callback(message, context):
    if message['message_type'] == "certificate_update":
        all_domains = message['data']['leaf_cert']['all_domains']
        for domain in all_domains:
            # Proveri da li domen sadrži ključne reči i da ne sadrži isključene reči
            if (any(re.search(keyword, domain.lower()) for keyword in keywords) and
                not any(exclude in domain.lower() for exclude in exclude_keywords)):

                print(f"\nPotencijalni sumnjiv domen: {domain}")

                # Provjera DNS-a
                dns_result = check_dns(domain)
                print(dns_result)

                # Provjera WHOIS informacija
                whois_result = check_whois(domain)
                print(whois_result)

                # Provjera HTTP statusa
                http_result = check_http_status(domain)
                print(http_result)

# Povezivanje na certstream i praćenje sertifikata
print("Povezivanje na certstream i praćenje sertifikata...")
certstream.listen_for_events(callback, url='wss://certstream.calidog.io')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)  # Ova linija treba biti uvučena

