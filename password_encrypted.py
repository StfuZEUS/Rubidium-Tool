#!/usr/bin/env python3
import os
import time
import hashlib
import bcrypt
import base64

# Colors
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
RESET  = "\033[0m"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

# Red Skull Art
print(f"{RED}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{RESET}")
print(f"{RED}⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀{RESET}")
print(f"{RED}⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⠟⠉⠀⠀⠀⠈⠙⠿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀{RESET}")
print(f"{RED}⠀⠀⠀⠀⠀⠀⢰⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀{RESET}")
print(f"{RED}⠀⠀⠀⠀⠀⠀⣸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⡇⠀⠀⠀⠀⠀⠀{RESET}")
print(f"{RED}⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀{RESET}")
print(f"{RED}⠀⠀⠀⠀⠀⠀⢿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⡇⠀⠀⠀⠀⠀⠀{RESET}")
print(f"{RED}⠀⠀⠀⠀⢠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⡀⠀⠀⠀⠀{RESET}")
print(f"{RED}⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠉⠉⠛⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀{RESET}")
print(f"{RED}⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀{RESET}")
print(f"{RED}⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡶⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀{RESET}")
print(f"{RED}⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀{RESET}")
print(f"{RED}⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀{RESET}")
print(f"{RED}⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣶⣶⣶⣶⣶⣾⣿⣿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀{RESET}")
print(f"{RED}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠛⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{RESET}\n")

print(f"{CYAN}[01]{GREEN} BCRYPT")
print(f"{CYAN}[02]{GREEN} MD5")
print(f"{CYAN}[03]{GREEN} SHA-1")
print(f"{CYAN}[04]{GREEN} SHA-256")
print(f"{CYAN}[05]{GREEN} PBKDF2")
print(f"{CYAN}[06]{GREEN} Base64 Encode{RESET}\n")

choice = input(f"{GREEN}[{time.strftime('%H:%M')}]{RED} [>]{GREEN} Choose   : {RESET}").strip()

if choice in ["01", "1"]:
    pwd = input(f"{GREEN}[{time.strftime('%H:%M')}]{RED} [>]{GREEN} Password To Encrypt : {RESET}")
    hashed = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt(rounds=12)).decode()
    print(f"{GREEN}[{time.strftime('%H:%M')}]{RED} [>]{GREEN} Encrypted Password  : {YELLOW}{hashed}{RESET}")

elif choice in ["02", "2"]:
    pwd = input(f"{GREEN}[{time.strftime('%H:%M')}]{RED} [>]{GREEN} Password To Encrypt : {RESET}")
    hashed = hashlib.md5(pwd.encode()).hexdigest()
    print(f"{GREEN}[{time.strftime('%H:%M')}]{RED} [>]{GREEN} Encrypted Password  : {YELLOW}{hashed}{RESET}")

elif choice in ["03", "3"]:
    pwd = input(f"{GREEN}[{time.strftime('%H:%M')}]{RED} [>]{GREEN} Password To Encrypt : {RESET}")
    hashed = hashlib.sha1(pwd.encode()).hexdigest()
    print(f"{GREEN}[{time.strftime('%H:%M')}]{RED} [>]{GREEN} Encrypted Password  : {YELLOW}{hashed}{RESET}")

elif choice in ["04", "4"]:
    pwd = input(f"{GREEN}[{time.strftime('%H:%M')}]{RED} [>]{GREEN} Password To Encrypt : {RESET}")
    hashed = hashlib.sha256(pwd.encode()).hexdigest()
    print(f"{GREEN}[{time.strftime('%H:%M')}]{RED} [>]{GREEN} Encrypted Password  : {YELLOW}{hashed}{RESET}")

elif choice in ["05", "5"]:
    pwd = input(f"{GREEN}[{time.strftime('%H:%M')}]{RED} [>]{GREEN} Password To Encrypt : {RESET}")
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', pwd.encode(), salt, 200000, dklen=32)
    final = salt.hex() + key.hex()
    print(f"{GREEN}[{time.strftime('%H:%M')}]{RED} [>]{GREEN} Encrypted Password  : {YELLOW}{final}{RESET}")

elif choice in ["06", "6"]:
    pwd = input(f"{GREEN}[{time.strftime('%H:%M')}]{RED} [>]{GREEN} Password To Encrypt : {RESET}")
    encoded = base64.b64encode(pwd.encode()).decode()
    print(f"{GREEN}[{time.strftime('%H:%M')}]{RED} [>]{GREEN} Encrypted Password  : {YELLOW}{encoded}{RESET}")

else:
    print(f"{RED}[!] Invalid option bhai!{RESET}")

input(f"\n{GREEN}Press Enter to exit...{RESET}")
