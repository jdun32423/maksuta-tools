import os
import time
import phonenumbers
import datetime
try:
    from zoneinfo import ZoneInfo
except ImportError:
    from pytz import timezone as ZoneInfo  # fallback, pip install pytz
from phonenumbers import (
    geocoder,
    carrier,
    timezone as tzmodule,
    PhoneNumberFormat,
    number_type as get_number_type,
)
from pystyle import Colors, Colorate
from pyfiglet import Figlet

TEXT_EXTS = [
    ".txt", ".csv", ".json", ".log", ".xml", ".yaml", ".yml",
    ".ini", ".conf", ".tsv", ".md", ".rst", ".html", ".htm",
    ".sql", ".dat", ".lst", ".cfg", ".dump", ".bak"
]

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def get_ascii_art():
    art = Figlet(font="slant").renderText("GhostLookup")
    return Colorate.Horizontal(Colors.red_to_purple, art)

def print_menu():
    print(Colors.red + """
[1] Поиск базовой информации по номеру
[2] Поиск в локальных базах данных
[3] Комбо-режим (1 + 2)
[0] Выход

by @zxc_defoltik for Kitaomi
""")

def basic_number_info(raw):
    clear()
    print(get_ascii_art())
    print(Colors.purple + "[ИНФОРМАЦИЯ О НОМЕРЕ]\n")
    try:
        pn = phonenumbers.parse(raw)
    except phonenumbers.NumberParseException as e:
        print(Colors.red + f"Ошибка разбора номера: {e}")
        input(Colors.green + "\nEnter — в меню...")
        return

    valid = phonenumbers.is_valid_number(pn)
    possible = phonenumbers.is_possible_number(pn)
    region = geocoder.description_for_number(pn, "ru")
    oper = carrier.name_for_number(pn, "ru")
    tz_list = tzmodule.time_zones_for_number(pn)
    nt = get_number_type(pn)
    intl = phonenumbers.format_number(pn, PhoneNumberFormat.INTERNATIONAL)
    natl = phonenumbers.format_number(pn, PhoneNumberFormat.NATIONAL)
    e164 = phonenumbers.format_number(pn, PhoneNumberFormat.E164)
    cc = pn.country_code
    is_geo = phonenumbers.is_number_geographical(pn)
    sms_ok = phonenumbers.is_possible_number_for_type(pn, phonenumbers.PhoneNumberType.MOBILE)
    
    print(Colors.cyan + "Результаты:")
    print(f"  {Colors.white}Корректен:            {valid}")
    print(f"  {Colors.white}Возможен:             {possible}")
    print(f"  {Colors.white}Регион:               {region}")
    print(f"  {Colors.white}Код страны:           +{cc}")
    print(f"  {Colors.white}Оператор:             {oper}")
    print(f"  {Colors.white}Тип номера:           {number_type_text(nt)}")
    print(f"  {Colors.white}Географический:       {is_geo}")
    print(f"  {Colors.white}SMS-пересылка:        {sms_ok}")
    print(f"  {Colors.white}Формат E164:          {e164}")
    print(f"  {Colors.white}Intl формат:          {intl}")
    print(f"  {Colors.white}Национальный формат:  {natl}")
    print(f"  {Colors.white}Часовые пояса:        {', '.join(tz_list)}")
    # Текущие времена в часовом поясе
    for zone in tz_list:
        try:
            now = datetime.datetime.now(ZoneInfo(zone))
            print(f"    – {zone}: {now.strftime('%Y-%m-%d %H:%M:%S')}")
        except Exception:
            pass

    input(Colors.green + "\nEnter — в меню...")

def search_in_files(target):
    clear()
    print(get_ascii_art())
    print(Colors.purple + "[ПОИСК В ЛОКАЛЬНЫХ БАЗАХ ДАННЫХ]\n")

    root = "C:\\" if os.name == "nt" else "/"
    file_list, total_bytes = [], 0

    print(Colors.yellow + "Сканирование файлов для статистики...")
    for dirpath, dirnames, filenames in os.walk(root):
        # исключаем системные каталоги на Windows и скрытые
        dirnames[:] = [d for d in dirnames if not d.startswith('.') and d.lower() not in ('windows','program files','program files (x86)')]
        for fn in filenames:
            if fn.lower().endswith(tuple(TEXT_EXTS)):
                full = os.path.join(dirpath, fn)
                file_list.append(full)
                try:
                    total_bytes += os.path.getsize(full)
                except:
                    pass

    total_files = len(file_list)
    total_mb = total_bytes / (1024**2)
    est_sec = total_mb / 20
    est_min = est_sec / 60
    print(Colors.cyan + f"\nФайлов: {total_files}, общий размер: {total_mb:.2f} MB")
    print(Colors.cyan + f"Оценочное время: {est_min:.1f} мин (~{est_sec:.0f} сек)\n")
    time.sleep(1.5)

    print(Colors.yellow + f"Ищем «{target}»...\n")
    found = 0
    for full in file_list:
        try:
            with open(full, "r", encoding="utf-8", errors="ignore") as f:
                for idx, line in enumerate(f, 1):
                    if target in line:
                        print(Colors.green + f"[НАЙДЕНО] {full} (стр.{idx}):")
                        print(Colors.white + "  " + line.strip())
                        found += 1
        except:
            continue

    if found:
        print(Colors.green + f"\nВсего совпадений: {found}")
    else:
        print(Colors.red + "\nСовпадений не найдено.")

    input(Colors.green + "\nEnter — в меню...")

def combo_mode():
    clear()
    print(get_ascii_art())
    print(Colors.purple + "[КОМБО-РЕЖИМ (1 + 2)]\n")
    raw = input(Colors.green + "Введите номер или текст для поиска: ").strip()
    basic_number_info(raw)
    search_in_files(raw)

def number_type_text(nt):
    m = {
        phonenumbers.PhoneNumberType.MOBILE: "Мобильный",
        phonenumbers.PhoneNumberType.FIXED_LINE: "Фиксированный",
        phonenumbers.PhoneNumberType.FIXED_LINE_OR_MOBILE: "Фикс./моб.",
        phonenumbers.PhoneNumberType.TOLL_FREE: "Бесплатный",
        phonenumbers.PhoneNumberType.PREMIUM_RATE: "Платный",
        phonenumbers.PhoneNumberType.SHARED_COST: "Разделённая стоимость",
        phonenumbers.PhoneNumberType.VOIP: "VoIP",
        phonenumbers.PhoneNumberType.PERSONAL_NUMBER: "Персональный",
        phonenumbers.PhoneNumberType.PAGER: "Пейджер",
        phonenumbers.PhoneNumberType.UAN: "UAN",
        phonenumbers.PhoneNumberType.VOICEMAIL: "Голосовая почта",
        phonenumbers.PhoneNumberType.UNKNOWN: "Неизвестный"
    }
    return m.get(nt, "Неизвестный")

def main():
    while True:
        clear()
        print(get_ascii_art())
        print_menu()
        choice = input(Colors.green + "Выберите опцию: ").strip()
        if choice == "1":
            raw = input(Colors.green + "Введите номер (+380...): ").strip()
            basic_number_info(raw)
        elif choice == "2":
            tgt = input(Colors.green + "Введите текст для поиска: ").strip()
            search_in_files(tgt)
        elif choice == "3":
            combo_mode()
        elif choice == "0":
            print(Colors.red + "\nВыход из программы...")
            break
        else:
            print(Colors.red + "Неверная команда.")
            time.sleep(1)

if __name__ == "__main__":
    main()
