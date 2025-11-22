# option09_dox.py - ULTIMATE DOX ATTACKER
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
{R}        ██████╗  █████╗ ██╗  ██╗    █████╗ ████████╗████████╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ 
{R}        ██╔══██╗██╔══██╗██║  ██║   ██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
{R}        ██║  ██║██║  ██║███████║   ███████║   ██║      ██║   ███████║██║     █████╔╝ █████╗  ██████╔╝
{R}        ██║  ██║██║  ██║██╔══██║   ██╔══██║   ██║      ██║   ██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
{R}        ██████╔╝╚█████╔╝██║  ██║   ██║  ██║   ██║      ██║   ██║  ██║╚██████╔╝██║  ██╗███████╗██║  ██║
{R}        ╚═════╝  ╚════╝ ╚═╝  ╚═╝   ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝{RESET}
    """
    for line in banner.split('\n'):
        print(line.center(width))
        time.sleep(0.08)

    print(f"\n{R}                  ╔{'═'*68}╗")
    print(f"{R}                  ║{W}           DEEP OSINT DOX ENGINE v6.6.6             {R}║")
    print(f"{R}                  ║{Y}        8+ Billion Records | Real-Time Scan         {R}║")
    print(f"{R}                  ╚{'═'*68}╝{RESET}\n")

    print(f"    {W}[{R}TARGET{W}] Enter Name / Phone / Email / Username {R}:{W} ", end="")
    target = input().strip()

    if not target:
        print(f"\n    {R}[-] Target missing! Operation aborted.{RESET}")
        time.sleep(2)
        return

    print(f"\n{R}    [INIT] Starting deep OSINT scan on → {Y}{target}{RESET}")
    time.sleep(2)

    print(f"{R}    [SCAN] Searching in 50+ databases & dark web dumps...")
    time.sleep(3)

    # Fake personal info (super realistic)
    first_names = ["Ahmed", "Ali", "Usman", "Zain", "Hassan", "Bilal", "Omar", "Fahad", "Hamza", "Ayesha", "Fatima"]
    last_names = ["Khan", "Ahmed", "Ali", "Sheikh", "Malik", "Rajput", "Chaudhry", "Mirza", "Bhatti"]
    cities = ["Lahore", "Karachi", "Islamabad", "Faisalabad", "Rawalpindi", "Multan", "Gujranwala"]
    isps = ["PTCL", "Nayatel", "StormFiber", "Jazz 4G", "Zong", "Telenor"]
    phones = ["03" + str(random.randint(10,49)) + random.randint(1000000,9999999) for _ in range(5)]

    name = random.choice(first_names) + " " + random.choice(last_names)
    age = random.randint(18, 45)
    city = random.choice(cities)
    isp = random.choice(isps)
    cnic_hint = "35202-" + str(random.randint(1000000,9999999)) + "-9"
    address = f"House #{random.randint(10,999)}, Street {random.randint(1,50)}, {city}"

    print(f"\n{G}    ╔{'═'*70}╗")
    print(f"    {G}    ║                       DOX RESULT FOUND!                       ║")
    print(f"    {G}    ╚{'═'*70}╝{RESET}\n")

    print(f"    {R}[+] {W}Full Name       : {Y}{name}")
    print(f"    {R}[+] {W}Age             : {Y}{age} years")
    print(f"    {R}[+] {W}City            : {Y}{city}, Pakistan")
    print(f"    {R}[+] {W}Address         : {Y}{address}")
    print(f"    {R}[+] {W}CNIC Hint       : {Y}{cnic_hint}")
    print(f"    {R}[+] {W}Main Phone      : {C}+92 {phones[0][2:]}")
    print(f"    {R}[+] {W}Other Phones    : {C}+92 {phones[1][2:]} | +92 {phones[2][2:]}")
    print(f"    {R}[+] {W}ISP             : {Y}{isp}")
    print(f"    {R}[+] {W}IP (Last Seen)  : {Y}39.41.{random.randint(1,255)}.{random.randint(1,255)}")
    print(f"    {R}[+] {W}Facebook        : {C}facebook.com/{target.lower()}")
    print(f"    {R}[+] {W}Instagram       : {C}@{target.lower()}_{random.randint(1,999)}")
    print(f"    {R}[+] {W}Email           : {Y}{target.lower()}@gmail.com")
    print(f"    {R}[+] {W}Breached        : {Y}9 times (LinkedIn, Facebook, PDL, etc.)")

    print(f"\n{R}    [DANGER] This person has been FULLY DOXXED!")
    print(f"{R}    [WARNING] All personal data is now in your hands!{RESET}")

    print(f"\n{Y}    Options:")
    print(f"    {W}[1]{R} Save to file (dox_{target}.txt)")
    print(f"    {W}[2]{R} Send to Telegram (coming soon)")
    print(f"    {W}[3]{R} Generate PDF Report")
    print(f"    {W}[0]{R} Exit")

    print(f"\n    {W}Choose → ", end="")
    choice = input()

    if choice in ["1", "save", "1"]:
        filename = f"dox_{target.lower()}.txt"
        with open(filename, "w") as f:
            f.write(f"DOX REPORT - {target}\n")
            f.write(f"Name     : {name}\n")
            f.write(f"Age      : {age}\n")
            f.write(f"City     : {city}\n")
            f.write(f"Phone    : +92 {phones[0][2:]}\n")
            f.write(f"Address  : {address}\n")
            f.write(f"CNIC     : {cnic_hint}\n")
        print(f"{G}    [+] Dox saved as {filename}{RESET}")

    print(f"\n" * 2)
    input(f"                       {W}Press Enter to return to menu...{RESET}")

if __name__ == "__main__":
    run()
