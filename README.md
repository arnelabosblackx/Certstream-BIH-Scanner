# Certstream-BIH-Scanner

## Opis
Certstream-BIH-Scanner je aplikacija koja prati SSL/TLS certifikate u realnom vremenu i skenira domene koristeći certstream za sumnjive aktivnosti vezane za ključne reči specifične za Bosnu i Hercegovinu. Pruža informacije o DNS-u, WHOIS i HTTP statusu.


## Instalacija
1. Klonirajte repozitorij:
   ```bash
   git clone https://github.com/arnelabosblackx/Certstream-BIH-Scanner.git

2. Pređite u direktorijum projekta:
   ```bash
   cd Certstream-BIH-Scanner
3. Instalirajte potrebne biblioteke:
   ```bash
   pip install -r requirements.txt
   
## Kako pokrenuti aplikaciju
Da pokrenete aplikaciju, koristite sledeću komandu:
```bash
python main.py

```
## Upotreba
Aplikacija pruža web interfejs za skeniranje domena. Unesite domen u formu i pritisnite "Skeniraj" da biste proverili njegove statusne informacije
`
## Zavisnosti
- Flask
- certstream
- python-whois
- requests

```
## Doprinos
Svi su dobrodošli da doprinesu projektu! Molimo vas da otvorite problem ili pošaljete zahtjev za povlačenje sa svojim prijedlozima.




