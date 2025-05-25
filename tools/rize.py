import os
import re
import ipaddress
import json
import xml.etree.ElementTree as ET
from datetime import datetime
from pyfiglet import Figlet
from pystyle import Colors, Colorate, Write
import phonenumbers
import validators

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def print_ascii_art():
    clear_console()
    fig = Figlet(font="slant")  # Любимый шрифт
    art = fig.renderText("RIZE")
    print(Colorate.Horizontal(Colors.red_to_purple, art))



def v_email(s):     return bool(re.fullmatch(r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+", s))
def v_phone(s):
    try: p=phonenumbers.parse(s,None); return phonenumbers.is_valid_number(p)
    except: return False
def v_ip(s):
    try: ipaddress.ip_address(s); return True
    except: return False
def v_ipv4(s):
    try: return isinstance(ipaddress.ip_address(s), ipaddress.IPv4Address)
    except: return False
def v_ipv6(s):
    try: return isinstance(ipaddress.ip_address(s), ipaddress.IPv6Address)
    except: return False
def v_url(s):       return validators.url(s)
def v_domain(s):    return bool(re.fullmatch(r"(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}", s))
def v_date(s):
    for fmt in ("%Y-%m-%d","%d.%m.%Y","%d/%m/%Y"):
        try: datetime.strptime(s,fmt); return True
        except: pass
    return False
def v_iso8601(s):
    try: datetime.fromisoformat(s); return True
    except: return False
def v_unix_ts(s):   return s.isdigit() and 0<=int(s)<=32503680000
def v_json(s):
    try: json.loads(s); return True
    except: return False
def v_xml(s):
    try: ET.fromstring(s); return True
    except: return False
def v_hex_color(s): return bool(re.fullmatch(r"#(?:[A-Fa-f0-9]{3}|[A-Fa-f0-9]{6})", s))
def v_rgb(s):      return bool(re.fullmatch(r"rgb\(\s*(?:[01]?\d?\d|2[0-4]\d|25[0-5])(?:,\s*(?:[01]?\d?\d|2[0-4]\d|25[0-5])){2}\s*\)", s))
def v_mac(s):      return bool(re.fullmatch(r"([0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}", s))
def v_slug(s):     return bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", s))
def v_password(s):
    return len(s)>=8 and re.search(r"[A-Z]",s) and re.search(r"[a-z]",s) and re.search(r"\d",s) and re.search(r"\W",s)
def v_uuid4(s):    return bool(re.fullmatch(r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-4[0-9a-fA-F]{3}-[89ABab][0-9a-fA-F]{3}-[0-9a-fA-F]{12}", s))
def v_uuid(s):     return bool(re.fullmatch(r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89ABab][0-9a-fA-F]{3}-[0-9a-fA-F]{12}", s))
def v_base64(s):   return bool(re.fullmatch(r"(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?", s))
def v_base32(s):   return bool(re.fullmatch(r"[A-Z2-7]+=*", s))
def v_md5(s):      return bool(re.fullmatch(r"[a-fA-F0-9]{32}", s))
def v_sha1(s):     return bool(re.fullmatch(r"[a-fA-F0-9]{40}", s))
def v_sha256(s):   return bool(re.fullmatch(r"[a-fA-F0-9]{64}", s))
def v_sha512(s):   return bool(re.fullmatch(r"[A-Fa-f0-9]{128}", s))
def v_email_dns(s):return v_email(s) and validators.domain(s.split("@")[1])
def v_passport(s): return bool(re.fullmatch(r"[A-Z]{2}\d{6}", s))
def v_inn_ua(s):   return bool(re.fullmatch(r"\d{10}", s))
def v_card(s):
    num=re.sub(r"\D","",s)
    if not re.fullmatch(r"\d{13,19}",num):return False
    def luhn(n):
        d=[int(x) for x in n];o=d[-1::-2];e=d[-2::-2]
        return (sum(o)+sum(sum(divmod(x*2,10)) for x in e))%10==0
    return luhn(num)
def v_cvv(s):      return bool(re.fullmatch(r"\d{3,4}", s))
def v_iban(s):     return bool(re.fullmatch(r"[A-Z]{2}\d{2}[A-Z0-9]{1,30}", s))
def v_vin(s):      return bool(re.fullmatch(r"[A-HJ-NPR-Z0-9]{17}", s))
def v_postal_us(s):return bool(re.fullmatch(r"\d{5}(?:-\d{4})?", s))
def v_postal_ru(s):return bool(re.fullmatch(r"\d{6}", s))
def v_country(s):  return bool(re.fullmatch(r"[A-Z]{2}", s))
def v_currency(s): return bool(re.fullmatch(r"[A-Z]{3}", s))
def v_lang(s):     return bool(re.fullmatch(r"[a-z]{2}(?:-[A-Z]{2})?", s))
def v_short_url(s):return bool(re.fullmatch(r"https?://(bit\.ly|t\.co|tinyurl\.com)/\S+", s))
def v_youtube_id(s):return bool(re.fullmatch(r"[A-Za-z0-9_-]{11}", s))
def v_telegram_username(s): return bool(re.fullmatch(r"@[A-Za-z0-9_]{5,32}", s))
def v_discord_tag(s): return bool(re.fullmatch(r".+?#\d{4}", s))
def v_hostname(s): return bool(re.fullmatch(r"(?!-)[A-Za-z0-9-]{1,63}(?<!-)(?:\.(?!-)[A-Za-z0-9-]{1,63}(?<!-))*", s))
def v_semver(s):   return bool(re.fullmatch(r"\d+\.\d+\.\d+(?:-[\w\.]+)?(?:\+[\w\.]+)?", s))
def v_doi(s):      return bool(re.fullmatch(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", s, re.I))
def v_issn(s):     return bool(re.fullmatch(r"\d{4}-\d{3}[\dX]", s))
def v_isbn10(s):   return bool(re.fullmatch(r"(?:(?:\d[\ |-]?){9}[\dX])", s))
def v_isbn13(s):   return bool(re.fullmatch(r"(?:(?:\d[\ |-]?){13})", s))
def v_morse(s):    return bool(re.fullmatch(r"[.\- ]+", s))
def v_cron(s):     return bool(re.fullmatch(r"(?:\*|[0-5]?\d)(?: (?:\*|[0-5]?\d)){4}", s))
def v_color_name(s): return s.lower() in ["red","green","blue","yellow","black","white","purple","orange"]
def v_filepath(s): return os.path.isabs(s)
def v_port(s):     return s.isdigit() and 0<=int(s)<=65535
def v_percentage(s): return bool(re.fullmatch(r"(?:100|[1-9]?\d)%", s))
def v_entity(s):   return bool(re.fullmatch(r"&[A-Za-z]+;", s))
def v_coords(s):   return bool(re.fullmatch(r"-?\d+(\.\d+)?,\s*-?\d+(\.\d+)?", s))
def v_yaml(s):     return s.strip().startswith("---")
def v_tweet(s):    return bool(re.fullmatch(r"https?://twitter\.com/.+/status/\d+", s))
def v_even(s):     return s.isdigit() and int(s)%2==0
def v_odd(s):      return s.isdigit() and int(s)%2==1
def v_csv(s):      return all(len(line.split(","))>1 for line in s.splitlines())

validators_list = [
    ("Email", v_email), ("Телефон", v_phone), ("IP общий", v_ip), ("IPv4", v_ipv4),
    ("IPv6", v_ipv6), ("URL", v_url), ("Домен", v_domain), ("Дата", v_date),
    ("ISO8601", v_iso8601), ("UNIX timestamp", v_unix_ts), ("JSON строка", v_json),
    ("XML строка", v_xml), ("Hex цвет", v_hex_color), ("RGB строка", v_rgb),
    ("MAC-адрес", v_mac), ("Slug", v_slug), ("Пароль сложный", v_password),
    ("UUID4", v_uuid4), ("UUID", v_uuid), ("Base64", v_base64),
    ("Base32", v_base32), ("MD5", v_md5), ("SHA1", v_sha1), ("SHA256", v_sha256),
    ("SHA512", v_sha512), ("Email+DNS", v_email_dns), ("Паспорт UA", v_passport),
    ("ИНН UA", v_inn_ua), ("Карта Luhn", v_card), ("CVV", v_cvv),
    ("IBAN", v_iban), ("VIN", v_vin), ("ZIP US", v_postal_us), ("Индекс RU", v_postal_ru),
    ("Код страны", v_country), ("Код валюты", v_currency), ("Код языка", v_lang),
    ("Short URL", v_short_url), ("YouTube ID", v_youtube_id), ("@Telegram", v_telegram_username),
    ("Discord tag", v_discord_tag), ("Hostname", v_hostname), ("SemVer", v_semver),
    ("DOI", v_doi), ("ISSN", v_issn), ("ISBN-10", v_isbn10), ("ISBN-13", v_isbn13),
    ("Morse", v_morse), ("Cron", v_cron), ("Color name", v_color_name),
    ("Абсолютный путь", v_filepath), ("Порт", v_port), ("Процент", v_percentage),
    ("HTML Entity", v_entity), ("Координаты", v_coords), ("YAML header", v_yaml),
    ("Tweet URL", v_tweet), ("Четное число", v_even), ("Нечетное число", v_odd),
    ("CSV контент", v_csv),
]

def main():
    print_ascii_art()
    Write.Print("\nпочему ты плачешь? почему рыдаешь? сам же выбрал страдать, а не вредить другим...\n",
                Colors.red_to_purple)
    Write.Print("👁️ Rize — ВАЛИДАТОР ВСЕГО. by @zxc_defoltik\n", Colors.red_to_purple)

    while True:
        print(Colorate.Horizontal(Colors.red_to_purple, "\n🔍 Что хочешь проверить?"))
        for i, (name, _) in enumerate(validators_list, 1):
            print(Colorate.Horizontal(Colors.red_to_purple, f"{i}. {name}"))
        print(Colorate.Horizontal(Colors.red_to_purple, "0. Выход"))

        choice = input(">>> ").strip()
        if choice == "0":
            Write.Print("Выход из Rize. До новой боли!\n", Colors.red_to_purple)
            break
        if not choice.isdigit() or not (1 <= int(choice) <= len(validators_list)):
            Write.Print("❌ Неверный выбор.\n", Colors.red_to_purple)
            continue

        idx = int(choice) - 1
        name, func = validators_list[idx]
        value = input(Colorate.Horizontal(Colors.red_to_purple, f"🔢 Введите {name}: ")).strip()
        try:
            ok = func(value)
            Write.Print(("✅ Валидно!\n" if ok else "❌ Не валидно.\n"), Colors.red_to_purple)
        except Exception as e:
            Write.Print(f"❌ Ошибка: {e}\n", Colors.red_to_purple)

if __name__ == "__main__":
    main()
