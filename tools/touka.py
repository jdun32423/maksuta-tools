import base64
import hashlib
import string
import random
import re
import sys
import time
import os
import textwrap
from collections import Counter
from cryptography.fernet import Fernet
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

PINK = '\033[95m'
LIGHT_PINK = '\033[91m'
WHITE = '\033[97m'
CYAN = '\033[96m'
BOLD = '\033[1m'
RESET = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    art = f"""
{PINK}{BOLD}  
       .==-.                   .-==.
        \\()8`-._  `.   .'  _.-'8()/
        (88""   ::.  \\./  .::   ""88)
         \\_.'`-::::.(#).::::-'`._/
           `._... .q(_)p. ..._.'
             ""-..-'|=|`-..-""
             .""' .'|=|`. `"".
           ,':8(o)./|=|\\.(o)8:`.
          (O :8 ::/ \\_/ \\:: 8: O)
           \\O `::/       \\::' O/
            ""--'         `--""
{WHITE}{BOLD}       Tōka ShadowText CLI Tool  🦋
"""
    print(art + RESET)

def wait(msg):
    for c in msg:
        sys.stdout.write(f"{LIGHT_PINK}{c}{RESET}")
        sys.stdout.flush()
        time.sleep(0.015)
    print()

def separator():
    print(f"\n{PINK}+{'-'*52}+{RESET}\n")

def reverse_text(t): return t[::-1]
def leetify(t): return t.translate(str.maketrans("aeiostAEIOST", "43105+43105+"))
def caesar_encrypt(t, shift): return ''.join(chr((ord(c) + shift) % 256) for c in t)
def caesar_decrypt(t, shift): return ''.join(chr((ord(c) - shift) % 256) for c in t)
def base64_encode(t): return base64.b64encode(t.encode()).decode()
def base64_decode(t): return base64.b64decode(t.encode()).decode(errors='ignore')
def remove_whitespace(t): return ''.join(t.split())
def remove_punctuation(t): return t.translate(str.maketrans('', '', string.punctuation))
def text_to_binary(t): return ' '.join(format(ord(c), '08b') for c in t)
def binary_to_text(t): return ''.join([chr(int(b, 2)) for b in t.split()])
def word_count(t): return len(t.split())
def char_count(t): return len(t)
def palindrome_check(t): return t == t[::-1]
def frequency_analysis(t): return Counter(t)
def random_case(t): return ''.join(random.choice([c.upper(), c.lower()]) for c in t)
def invisible_text(t): return ''.join(c + '\u200b' for c in t)
def text_hash(t, algo='sha256'):
    h = getattr(hashlib, algo)()
    h.update(t.encode())
    return h.hexdigest()
def ascii_artify(t): return '\n'.join(textwrap.wrap("".join([f"{ord(c):02x}" for c in t]), 16))
def text_noise(t): return ''.join(c + random.choice('!@#$%^&*') for c in t)
def clean_links(t): return re.sub(r'http[s]?://\\S+', '', t)
def shuffle_text(t): 
    l = list(t)
    random.shuffle(l)
    return ''.join(l)
def emphasize_vowels(t):
    vowels = "aeiouAEIOU"
    return ''.join(f"{LIGHT_PINK}{c}{RESET}" if c in vowels else c for c in t)
def count_sentences(t):
    return len(re.findall(r'[.!?]+', t))
def remove_digits(t):
    return ''.join(c for c in t if not c.isdigit())
def swap_case(t):
    return t.swapcase()

def aes_encrypt(t, key):
    cipher = AES.new(key.encode('utf-8').ljust(32, b'0'), AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(t.encode(), AES.block_size))
    return base64.b64encode(cipher.iv + ct_bytes).decode()

def xor_encrypt(t, key):
    return ''.join(chr(ord(c)^ord(key[i%len(key)])) for i,c in enumerate(t))

def vigenere_encrypt(t, key):
    return ''.join(chr((ord(c) + ord(key[i%len(key)])) % 256) for i,c in enumerate(t))

def rot13_encrypt(t):
    return t.translate(str.maketrans(
        'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
        'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'))

def fernet_encrypt(t, fkey):
    f = Fernet(fkey)
    return f.encrypt(t.encode()).decode()

def aes_decrypt(t, key):
    raw = base64.b64decode(t)
    iv, ct = raw[:16], raw[16:]
    cipher = AES.new(key.encode('utf-8').ljust(32, b'0'), AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ct), AES.block_size).decode()

def xor_decrypt(t, key):
    return xor_encrypt(t, key)

def vigenere_decrypt(t, key):
    return ''.join(chr((ord(c) - ord(key[i%len(key)])) % 256) for i,c in enumerate(t))

def rot13_decrypt(t):
    return rot13_encrypt(t)

def fernet_decrypt(t, fkey):
    f = Fernet(fkey)
    return f.decrypt(t.encode()).decode()

def print_menu():
    clear_screen()
    separator()
    banner()
    print(f"{PINK}{BOLD}Tōka Functions:{RESET}")
    funcs = [
        "1  - reverse_text(text)",
        "2  - leetify(text)",
        "3  - caesar_encrypt(text, shift)",
        "4  - caesar_decrypt(text, shift)",
        "5  - base64_encode(text)",
        "6  - base64_decode(text)",
        "7  - remove_whitespace(text)",
        "8  - remove_punctuation(text)",
        "9  - text_to_binary(text)",
        "10 - binary_to_text(text)",
        "11 - word_count(text)",
        "12 - char_count(text)",
        "13 - palindrome_check(text)",
        "14 - frequency_analysis(text)",
        "15 - random_case(text)",
        "16 - invisible_text(text)",
        "17 - text_hash(text, algo='sha256')",
        "18 - ascii_artify(text)",
        "19 - text_noise(text)",
        "20 - clean_links(text)",
        "21 - shuffle_text(text)",
        "22 - emphasize_vowels(text)",
        "23 - count_sentences(text)",
        "24 - remove_digits(text)",
        "25 - swap_case(text)",
        "26 - aes_encrypt(text, key)",
        "27 - xor_encrypt(text, key)",
        "28 - vigenere_encrypt(text, key)",
        "29 - rot13_encrypt(text)",
        "30 - fernet_encrypt(text, fkey)",
        "31 - aes_decrypt(text, key)",
        "32 - xor_decrypt(text, key)",
        "33 - vigenere_decrypt(text, key)",
        "34 - rot13_decrypt(text)",
        "35 - fernet_decrypt(text, fkey)"
    ]
    for f in funcs:
        print(f"{LIGHT_PINK}{f}{RESET}")
    separator()

def get_input(prompt):
    return input(f"{WHITE}{prompt}{RESET}")

def main():
    while True:
        print_menu()
        choice = get_input("Choose function number (or 'exit' to quit): ").strip()
        if choice.lower() in ('exit', 'quit'):
            print(f"{PINK}Goodbye! 🦋{RESET}")
            break
        if not choice.isdigit() or not (1 <= int(choice) <= 35):
            print(f"{LIGHT_PINK}Invalid choice, try again.{RESET}")
            time.sleep(1.2)
            continue
        fn_num = int(choice)

        try:
            if fn_num in range(1, 26):
                text = get_input("Enter text: ")
                if fn_num in (3,4):
                    shift = int(get_input("Enter shift number: "))
                if fn_num == 17:
                    algo = get_input("Enter hash algorithm (default sha256): ") or 'sha256'

                if fn_num == 1: result = reverse_text(text)
                elif fn_num == 2: result = leetify(text)
                elif fn_num == 3: result = caesar_encrypt(text, shift)
                elif fn_num == 4: result = caesar_decrypt(text, shift)
                elif fn_num == 5: result = base64_encode(text)
                elif fn_num == 6: result = base64_decode(text)
                elif fn_num == 7: result = remove_whitespace(text)
                elif fn_num == 8: result = remove_punctuation(text)
                elif fn_num == 9: result = text_to_binary(text)
                elif fn_num == 10: result = binary_to_text(text)
                elif fn_num == 11: result = str(word_count(text))
                elif fn_num == 12: result = str(char_count(text))
                elif fn_num == 13: result = str(palindrome_check(text))
                elif fn_num == 14:
                    freq = frequency_analysis(text)
                    result = "\n".join(f"{c!r}: {cnt}" for c,cnt in freq.most_common())
                elif fn_num == 15: result = random_case(text)
                elif fn_num == 16: result = invisible_text(text)
                elif fn_num == 17: result = text_hash(text, algo)
                elif fn_num == 18: result = ascii_artify(text)
                elif fn_num == 19: result = text_noise(text)
                elif fn_num == 20: result = clean_links(text)
                elif fn_num == 21: result = shuffle_text(text)
                elif fn_num == 22: result = emphasize_vowels(text)
                elif fn_num == 23: result = str(count_sentences(text))
                elif fn_num == 24: result = remove_digits(text)
                elif fn_num == 25: result = swap_case(text)

            elif fn_num in range(26, 31):
                text = get_input("Enter text: ")
                key = get_input("Enter key: ")
                if fn_num == 26: result = aes_encrypt(text, key)
                elif fn_num == 27: result = xor_encrypt(text, key)
                elif fn_num == 28: result = vigenere_encrypt(text, key)
                elif fn_num == 29: result = rot13_encrypt(text)
                elif fn_num == 30:
                    try:
                        fkey = key.encode()
                        result = fernet_encrypt(text, key)
                    except Exception as e:
                        result = f"Error in Fernet encrypt: {e}"

            elif fn_num in range(31, 36):
                text = get_input("Enter encrypted text: ")
                key = get_input("Enter key: ")
                if fn_num == 31:
                    try: result = aes_decrypt(text, key)
                    except Exception as e: result = f"Decryption error: {e}"
                elif fn_num == 32: result = xor_decrypt(text, key)
                elif fn_num == 33: result = vigenere_decrypt(text, key)
                elif fn_num == 34: result = rot13_decrypt(text)
                elif fn_num == 35:
                    try: result = fernet_decrypt(text, key)
                    except Exception as e: result = f"Decryption error: {e}"

            else:
                result = "Unknown function."

            separator()
            print(f"{CYAN}{BOLD}Result:{RESET}\n\n{result}\n")
            separator()
            input(f"{PINK}Press ENTER to return to menu...{RESET}")

        except Exception as e:
            print(f"{LIGHT_PINK}Error: {e}{RESET}")
            input(f"{PINK}Press ENTER to return to menu...{RESET}")

if __name__ == "__main__":
    main()