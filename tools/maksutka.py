import requests
from bs4 import BeautifulSoup
import re
import socket
from colorama import Fore, init
from random import choice, randint
import os
import pyfiglet
import requests
from bs4 import BeautifulSoup
import re
import socket
import requests
import re
from colorama import Fore, init
from random import choice
import random
import time
import os
from bs4 import BeautifulSoup
import pyfiglet 

init(autoreset=True)
os.system('cls' if os.name == 'nt' else 'clear')

def banner_menuu():
    return pyfiglet.figlet_format("maksutka", font="slant")

def color_transition(text, colors):
    result = ""
    color_index = 0
    for char in text:
        if char.strip():
            result += f"{colors[color_index]}{char}"
            color_index = (color_index + 1) % len(colors)
        else:
            result += char
    return result

def print_banner():
    colorssss = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.MAGENTA, Fore.BLUE]
    bannerrrrr = banner_menu()
    print(color_transition(bannerrrrr, colorssss))

def search_vk(name, surname):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    query = f"{name}+{surname}+site:vk.com"
    url = f"https://www.google.com/search?q={query}"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True) if 'vk.com' in a['href']]
        if links:
            print(Fore.GREEN + "🔎 Знайдено профілі VK:")
            for link in set(links):
                print(Fore.CYAN + link)
        else:
            print(Fore.RED + "❌ VK профілі не знайдено.")
    except Exception as e:
        print(Fore.RED + f"[ПОМИЛКА VK] {e}")

def generate_passport():
    names = ['Ivan', 'Oleg', 'Maksym', 'Dmytro', 'Olena', 'Natalia']
    surnames = ['Shevchenko', 'Koval', 'Bondarenko', 'Tkachenko', 'Melnyk']
    patronymics = ['Ivanovych', 'Petrovych', 'Olehovych', 'Serhiyovych', 'Andriyivna', 'Volodymyrivna']
    region = choice(['Київ', 'Львів', 'Одеса', 'Харків', 'Дніпро', 'Запоріжжя'])
    full_name = f"{choice(surnames)} {choice(names)} {choice(patronymics)}"
    dob = f"{randint(1, 28):02d}.{randint(1, 12):02d}.{randint(1965, 2003)}"
    series = f"{choice(['АН', 'ВМ', 'СЕ', 'КВ'])}"
    number = f"{randint(100000, 999999)}"
    code = f"{randint(1000, 9999)}"
    return (
        f"{Fore.CYAN}🆔 Генерація паспорта:\n"
        f"👤 ПІБ: {full_name}\n"
        f"📅 Дата народження: {dob}\n"
        f"📍 Місце реєстрації: {region}\n"
        f"📄 Серія/Номер: {series} {number}\n"
        f"🏢 Код підрозділу: {code}"
    )

def search_in_database(query):
    fake_db = {
        "maks": ["maks_1999", "maks_login", "maksutka1337"],
        "ivan": ["ivanov1987", "ivchik", "ivanko"],
        "natalia": ["nata_2002", "natali_star", "natkova"],
        "oleg": ["oleg228", "oleg_real", "oleg_work"]
    }
    query = query.lower()
    results = fake_db.get(query, [])
    if results:
        return f"{Fore.GREEN}✅ Результати для '{query}':\n" + "\n".join(Fore.CYAN + x for x in results)
    return f"{Fore.RED}❌ Жодного результату для запиту: {query}"

def get_ip_info(ip):
    try:
        host, aliases, addresses = socket.gethostbyaddr(ip)
        return (
            f"{Fore.GREEN}🛰️ Інформація про IP:\n"
            f"🌐 Хост: {Fore.CYAN}{host}\n"
            f"🔁 Псевдоніми: {', '.join(aliases) if aliases else 'Немає'}\n"
            f"📡 Адреси: {', '.join(addresses)}"
        )
    except socket.herror:
        return f"{Fore.RED}❌ Не вдалося отримати дані по IP: {ip}"
    except Exception as e:
        return f"{Fore.RED}⚠️ Помилка: {str(e)}"

def get_email_info(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.fullmatch(pattern, email):
        domain = email.split("@")[1]
        provider = {
            "gmail.com": "Google Mail",
            "ukr.net": "UkrNet",
            "meta.ua": "Meta.ua",
            "outlook.com": "Microsoft Outlook",
            "i.ua": "I.UA"
        }.get(domain, "Невідомий поштовий сервіс")
        return (
            f"{Fore.GREEN}📧 Email коректний: {Fore.CYAN}{email}\n"
            f"🌐 Домен: {domain}\n"
            f"📬 Сервіс: {provider}"
        )
    return f"{Fore.RED}❌ Email має некоректний формат: {email}"

def get_phone_info(phone):
    pattern = r"^\+380\d{9}$"
    operator_map = {
        "50": "Vodafone",
        "66": "Vodafone",
        "95": "Vodafone",
        "99": "Vodafone",
        "67": "Kyivstar",
        "68": "Kyivstar",
        "96": "Kyivstar",
        "97": "Kyivstar",
        "98": "Kyivstar",
        "63": "Lifecell",
        "73": "Lifecell",
        "93": "Lifecell"
    }
    if re.fullmatch(pattern, phone):
        code = phone[3:5]
        operator = operator_map.get(code, "Невідомий оператор")
        return (
            f"{Fore.GREEN}📱 Телефон коректний: {Fore.CYAN}{phone}\n"
            f"📶 Оператор: {operator}"
        )
    return f"{Fore.RED}❌ Невірний формат телефону: {phone}"

def banner_menu():
   ascii_art = print(pyfiglet.figlet_format("          maksutka"))

import phonenumbers
import hashlib
import base64
import socket
import datetime
import re
import dns.resolver
import os
import platform
from phonenumbers import geocoder, carrier, timezone

class colorssss:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def system_info():
    os_info = platform.system() + " " + platform.release()
    local_ip = socket.gethostbyname(socket.gethostname())
    launch_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return os_info, local_ip, launch_time

def analyze_number(number):
    parsed = phonenumbers.parse(number, None)
    info = {
        "is_valid": phonenumbers.is_valid_number(parsed),
        "is_possible": phonenumbers.is_possible_number(parsed),
        "region": geocoder.description_for_number(parsed, "uk"),
        "carrier": carrier.name_for_number(parsed, "uk"),
        "timezones": timezone.time_zones_for_number(parsed)
    }
    return info

def osint_links(number):
    clean_number = re.sub(r'\D', '', number)
    return {
        "Google": f"https://www.google.com/search?q={clean_number}",
        "Facebook": f"https://www.facebook.com/search/top?q={clean_number}",
        "LinkedIn": f"https://www.linkedin.com/search/results/all/?keywords={clean_number}",
        "WhoCalled": f"https://who-called.co.uk/Number/{clean_number}",
        "Spamcalls.net": f"https://spamcalls.net/en/number/{clean_number}",
        "Numinfo": f"https://numinfo.net/{clean_number}"
    }

def check_messengers(number):
    result = {}
    platforms = ["Telegram", "WhatsApp", "Viber", "Signal"]
    for platform in platforms:
        result[platform] = f"Перевірити вручну або API ({platform.lower()}.me/{number[-9:]})"
    return result

def digit_analysis(number):
    digits = re.sub(r'\D', '', number)
    freq = {str(i): digits.count(str(i)) for i in range(10)}
    return {
        "length": len(digits),
        "sum": sum(int(d) for d in digits),
        "frequencies": freq,
        "is_palindrome": digits == digits[::-1]
    }


def hash_data(data):
    encoded = data.encode()
    return {
        "MD5": hashlib.md5(encoded).hexdigest(),
        "SHA1": hashlib.sha1(encoded).hexdigest(),
        "SHA256": hashlib.sha256(encoded).hexdigest(),
        "BASE64": base64.b64encode(encoded).decode()
    }


def dns_lookup(domain="google.com"):
    try:
        answers = dns.resolver.resolve(domain, 'A')
        return [rdata.address for rdata in answers]
    except:
        return ["Помилка DNS"]


def print_report(number):

    print(f"{Colors.OKCYAN}[1] Аналіз формату, гео та оператора...{Colors.ENDC}")
    info = analyze_number(number)
    for k, v in info.items():
        print(f"  {k.capitalize()}: {v}")

    print(f"{Colors.OKCYAN}\n[2] OSINT посилання:{Colors.ENDC}")
    links = osint_links(number)
    for name, url in links.items():
        print(f"  {name}: {url}")

    print(f"{Colors.OKCYAN}\n[3] Перевірка месенджерів:{Colors.ENDC}")
    messengers = check_messengers(number)
    for m, res in messengers.items():
        print(f"  {m}: {res}")

    print(f"{Colors.OKCYAN}\n[4] Цифрова аналітика:{Colors.ENDC}")
    digits = digit_analysis(number)
    for k, v in digits.items():
        print(f"  {k.capitalize()}: {v}")

    print(f"{Colors.OKCYAN}\n[5] Хеші номера:{Colors.ENDC}")
    hashes = hash_data(number)
    for algo, h in hashes.items():
        print(f"  {algo}: {h}")

    print(f"{Colors.OKCYAN}\n[6] DNS Lookup:{Colors.ENDC}")
    dns_res = dns_lookup()
    for ip in dns_res:
        print(f"  IP: {ip}")

    print(f"{Colors.OKCYAN}\n[7] Аналіз завершено.{Colors.ENDC}\n")


def phonenum():
    print(" by @zxc_defoltik ")
    print("\nВведи номер у форматі +380XXXXXXXXX:")
    number = input(">>> ").strip()
    if not re.match(r'^\+380\d{9}$', number):
        print(f"{Colors.FAIL}Неправильний формат номера!{Colors.ENDC}")
        return
    print_report(number)

def qqqqqwwwwmaksutka():
    banner_menuu()
    print("                         by @zxc_defoltik ")
    time.sleep(2)  # Затримка для гарного відображення

    while True:
        print(Fore.RED + "\n                         Choose an option:")
        print(Fore.RED + "                         1. Search VK Profile")
        print(Fore.RED + "                         2. Generate Passport")
        print(Fore.RED + "                         3. Search in Database")
        print(Fore.RED + "                         4. Get IP Info")
        print(Fore.RED + "                         5. Get Email Info")
        print(Fore.RED + "                         6. Get Phone Info")
        print(Fore.RED + "                         7. Exit")

        choice = input("> ")

        if choice == "1":
            name = input("Enter first name: ")
            surname = input("Enter last name: ")
            # Виклик функції пошуку VK
            print(f"Searching VK profile for {name} {surname}...")
            search_vk(name, surname)
        elif choice == "2":
            # Генерація паспорта
            print(generate_passport())
        elif choice == "3":
            # Пошук у базі даних
            query = input("Enter query to search in database: ")
            print(search_in_database(query))
        elif choice == "4":
            ip = input("Enter IP to lookup: ")
            print(get_ip_info(ip))
        elif choice == "5":
            email = input("Enter email to validate: ")
            print(get_email_info(email))
        elif choice == "6":
            phonenum()
        elif choice == "7":
            print(Fore.RED + "Exiting...")
            break
        else:
            print(Fore.RED + "Invalid choice. Please select a valid option.")

qqqqqwwwwmaksutka()
