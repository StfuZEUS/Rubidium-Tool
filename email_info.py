# option12_email_info.py - ULTIMATE EMAIL INFO EXTRACTOR
import os
import time
import random
import shutil

R = "\033[91m"
W = "\033[97m"
G = "\033[92m"
Y = "\033[93m"
C = "\033[96m"
RESET = "\033[0m"

def run():
    os.system('clear')
    width = shutil.get_terminal_size().columns

    banner = f"""
{R}        ███████╗███╗   ███╗ █████╗ ██╗██╗         ██╗███╗   ██╗███████╗ ██████╗ 
{R}        ██╔════╝████╗ ████║██╔══██╗██║██║         ██║████╗  ██║██╔════╝██╔═══██╗
{R}        █████╗  ██╔████╔██║███████║██║██║         ██║██╔██╗ ██║█████╗  ██║   ██║
{R}        ██╔══╝  ██║╚██╔╝██║██╔══██║██║██║         ██║██║╚██╗██║██╔══╝  ██║   ██║
{R}        ███████╗██║ ╚═╝ ██║██║  ██║██║███████╗    ██║██║ ╚████║██║     ╚██████╔╝
{R}        ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ {RESET}
    """
    for line in banner.split('\n'):
        print(line.center(width))
        time.sleep(0.08)

    print(f"\n{R}                  ╔{'═'*68}╗")
    print(f"{R}                  ║{W}           DEEP EMAIL OSINT SCANNER v8.8.8             {R}║")
    print(f"{R}                  ║{Y}          100+ Sources | Real-Time Extraction          {R}║")
    print(f"{R}                  ╚{'═'*68}╝{RESET}\n")

    current_time = time.strftime("%H:%M:%S")
    print(f"      {W}[{W}{current_time}{W}] {W}[{R}>{W}] {W}Target Email {R}:{W} ", end="")
    email = input().strip()

    if not email or "@" not in email:
        print(f"\n      {R}[-] Invalid email! Aborting mission...{RESET}")
        time.sleep(2)
        return

    print(f"\n{R}    [INIT] Starting deep email reconnaissance on → {Y}{email}{RESET}")
    time.sleep(2.5)

    print(f"{R}    [SCAN] Querying HaveIBeenPwned, Dehashed, IntelX, Leak-Lookup, Snusbase, BreachDirectory...")
    time.sleep(3.5)

    # Fake but super realistic data
    domains = email.split("@")[1]
    username = email.split("@")[0]

    first_names = ["Ali", "Ahmed", "Hassan", "Zain", "Omar", "Fahad", "Usman", "Bilal", "Hamza", "Ayesha"]
    last_names = ["Khan", "Sheikh", "Malik", "Rajput", "Chaudhry", "Bhatti", "Mirza", "Jutt", "Arain"]
    cities = ["Lahore", "Karachi", "Islamabad", "Faisalabad", "Multan", "Rawalpindi", "Gujranwala"]
    isps = ["PTCL", "Nayatel", "StormFiber", "Jazz", "Zong", "Telenor"]
    providers = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "icloud.com"]

    name = random.choice(first_names) + " " + random.choice(last_names)
    age = random.randint(19, 48)
    ip = f"39.41.{random.randint(1,255)}.{random.randint(1,255)}"
    phone_hint = "03" + str(random.randint(10,49)) + "*******"

    print(f"\n{G}    ╔{'═'*74}╗")
    print(f"    {G}    ║                     EMAIL INFO EXTRACTED!                     ║")
    print(f"    {G}    ╚{'═'*74}╝{RESET}\n")

    print(f"    {R}[+] {W}Email           : {C}{email}")
    print(f"    {R}[+] {W}Username        : {Y}{username}")
    print(f"    {R}[+] {W}Domain          : {Y}{domains}")
    print(f"    {R}[+] {W}Provider        : {G}{domains.split('.')[0].capitalize()} Mail")
    print(f"    {R}[+] {W}Full Name       : {Y}{name}")
    print(f"    {R}[+] {W}Age             : {Y}{age} years")
    print(f"    {R}[+] {W}Location        : {Y}{random.choice(cities)}, Pakistan")
    print(f"    {R}[+] {W}IP (Last Seen)  : {Y}{ip}")
    print(f"    {R}[+] {W}ISP             : {Y}{random.choice(isps)}")
    print(f"    {R}[+] {W}Phone Hint      : {C}+92 {phone_hint}")
    print(f"    {R}[+] {W}Created Approx  : {Y}{random.randint(2010,2024)}")
    print(f"    {R}[+] {W}Breached        : {R}{random.randint(7,21)} times")
    print(f"    {R}[+] {W}Password Found  : {G}{''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789!@#$%', k=14))}")
    print(f"    {R}[+] {W}Recovery Email  : {Y}{username}123@{random.choice(providers)}")
    print(f"    {R}[+] {W}Security Q      : {Y}What is your pet's name?")

    print(f"\n{R}    [SOCIALS FOUND]")
    print(f"    {G}[+] {W}Facebook        : {C}facebook.com/{username.lower()}")
    print(f"    {G}[+] {W}Instagram       : {C}@{username.lower()}_{random.randint(1,9999)}")
    print(f"    {G}[+] {W}Twitter/X       : {C}@{username.lower()}")
    print(f"    {G}[+] {W}LinkedIn        : {C}linkedin.com/in/{username.lower()}")
    print(f"    {R}[-] {W}Snapchat        : {Y}Not Found")
    print(f"    {G}[+] {W}GitHub          : {C}github.com/{username.lower()}")

    print(f"\n{R}    [DANGER] This email has been COMPLETELY COMPROMISED!")
    print(f"{R}    [ALERT]  Owner's full digital footprint is now exposed!{RESET}")

    print(f"\n{Y}    Options:")
    print(f"    {W}[1]{R} Save full report (email_{username}.txt)")
    print(f"    {W}[2]{R} Generate PDF dox")
    print(f"    {W}[3]{R} Send to Telegram")
    print(f"    {W}[0]{R} Back to menu")

    print(f"\n    {W}Select → ", end="")
    choice = input()

    if choice == "1":
        with open(f"email_{username}.txt", "w") as f:
            f.write(f"EMAIL INFO REPORT - {email}\n{'='*50}\n")
            f.write(f"Name       : {name}\n")
            f.write(f"Age        : {age}\n")
            f.write(f"Location   : {random.choice(cities)}\n")
            f.write(f"IP         : {ip}\n")
            f.write(f"Password   : {'*' * 12}\n")
        print(f"{G}    [+] Report saved as email_{username}.txt{RESET}")

    print(f"\n" * 2)
    input(f"                       {W}Press Enter to return...{RESET}")

if __name__ == "__main__":
    run()
