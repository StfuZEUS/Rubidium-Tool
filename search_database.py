# option07_database_search.py
import os
import time
import random
import shutil

R = "\033[91m"
W = "\033[97m"
G = "\033[92m"
Y = "\033[93m"
RESET = "\033[0m"

def run():
    os.system('clear')
    width = shutil.get_terminal_size().columns

    banner = f"""
{R}    ██████╗  █████╗ ████████╗ █████╗ ██████╗  █████╗ ███████╗███████╗
{R}    ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝
{R}    ██║  ██║███████║   ██║   ███████║██████╔╝███████║███████╗█████╗  
{R}    ██║  ██║██╔══██║   ██║   ██╔══██║██╔══██╗██╔══██║╚════██║██╔══╝  
{R}    ██████╔╝██║  ██║   ██║   ██║  ██║██████╔╝██║  ██║███████║███████╗
{R}    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝{RESET}
    """
    for line in banner.split('\n'):
        print(line.center(width))
        time.sleep(0.08)

    print(f"\n{R}                ╔{'═'*62}╗")
    print(f"{R}                ║{W}        BREACHED DATABASE SEARCH ENGINE           {R}║")
    print(f"{R}                ║{Y}      50+ Billion Records | 2025 Updated          {R}║")
    print(f"{R}                ╚{'═'*62}╝{RESET}\n")

    print(f"    {W}[{R}TYPE{W}] {Y}1. Email    {Y}2. Phone    {Y}3. Username    {Y}4. Name")
    print(f"    {W}[{R}>{W}] Choose: ", end="")
    choice = input().strip()

    print(f"\n    {W}[{R}TARGET{W}] Enter your target {R}:{W} ", end="")
    target = input().strip()

    if not target:
        print(f"\n    {R}[-] Empty input! Aborting...{RESET}")
        time.sleep(2)
        return

    print(f"\n{R}    [SEARCHING] Scanning 50+ breached databases...{RESET}")
    time.sleep(2.5)

    print(f"{R}    [DATABASES] Checking: CombiNation, BreachCompilation, AntiPublic, Exploit.in, RaidForums Legacy...")
    time.sleep(2)

    # Fake results — super realistic
    found = random.choice([True, True, False, True])  # 75% chance found

    if found:
        print(f"{G}    [+] TARGET FOUND IN MULTIPLE BREACHES!{RESET}\n")
        breaches = random.sample([
            "Collection #1-5", "BreachCompilation", "AntiPublic", "Exploit.in", 
            "Verifications.io", "Cit0day", "LinkedIn 2021", "Facebook 2021", "PDL 2023"
        ], k=random.randint(2,5))

        for breach in breaches:
            password = "".join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*", k=12))
            print(f"    {R}[+] {W}{breach}")
            print(f"        {Y}Email    : {target}")
            print(f"        {Y}Password : {password}")
            print(f"        {Y}Hash     : md5 / sha1 / bcrypt")
            print(f"        {Y}Source   : {breach} | Leaked: {random.randint(2019,2025)}\n")
            time.sleep(0.8)

        print(f"{R}    [WARNING] This user has been PWNED {len(breaches)} times!")
        print(f"{R}    [ADVICE]  Immediately change all passwords!{RESET}")

    else:
        print(f"{Y}    [-] No results found in known breaches.")
        print(f"{Y}    [-] This target is clean (for now)...{RESET}")

    print("\n" * 2)
    input(f"                       {W}Press Enter to continue...{RESET}")

if __name__ == "__main__":
    run()
