# option08_ddos.py
import os
import time
import random
import threading
import shutil

R = "\033[91m"
W = "\033[97m"
G = "\033[92m"
Y = "\033[93m"
RESET = "\033[0m"

def fake_logs():
    methods = ["HTTP/2 FLOOD", "SLOWLORIS", "UDP STORM", "SYN FLOOD", "DNS AMP", "NTP AMP", "OVH BYPASS", "CLOUDFLARE KILLER", "LAYER 7 BLAST"]
    while threading.main_thread().is_alive():
        packets = random.randint(100000, 9999999)
        gbps = round(random.uniform(100, 3500), 2)
        print(f"   {R}[{Y}ATTACK{R}] {G}{random.choice(methods)}{R} → {W}{gbps} Gbps {R}| {Y}{packets:,} pps", flush=True)
        time.sleep(0.18)

def run():
    os.system('clear')
    width = shutil.get_terminal_size().columns

    print(f"{R}    ██████╗ ██████╗  █████╗  ██████╗ {RESET}".center(width))
    print(f"{R}    ██╔══██╗██╔══██╗██╔══██╗██╔════╝{RESET}".center(width))
    print(f"{R}    ██║  ██║██║  ██║███████║██║  ███╗{RESET}".center(width))
    print(f"{R}    ██║  ██║██║  ██║██╔══██║██║   ██║{RESET}".center(width))
    print(f"{R}    ██████╔╝██████╔╝██║  ██║╚██████╔╝{RESET}".center(width))
    print(f"{R}    ╚═════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ {RESET}".center(width))
    time.sleep(1)

    print(f"\n{R}                  ╔{'═'*60}╗")
    print(f"{R}                  ║{W}           ULTIMATE DDoS PANEL v9.0             {R}║")
    print(f"{R}                  ║{Y}         LAYER 4 + LAYER 7 | 3500+ Gbps         {R}║")
    print(f"{R}                  ╚{'═'*60}╝{RESET}\n")

    print(f"    {W}[{R}TARGET{W}] IP / URL {R}:{W} ", end="")
    target = input().strip() or "192.168.1.1"

    print(f"    {W}[{R}PORT{W}] Port (default: random) {R}:{W} ", end="")
    port = input().strip() or "Random"

    print(f"    {W}[{R}TIME{W}] Duration (sec) {R}:{W} ", end="")
    duration = input().strip() or "600"

    print(f"\n{R}    ╔{'═'*62}╗")
    print(f"    {R}    ║{W} TARGET   → {target:<46} {R}║")
    print(f"    {R}    ║{W} PORT     → {port:<46} {R}║")
    print(f"    {R}    ║{W} TIME     → {duration} seconds{' '*30} {R}║")
    print(f"    {R}    ║{W} POWER    → MAX (3500+ Gbps){' '*28} {R}║")
    print(f"    {R}    ╚{'═'*62}╝\n")

    print(f"{R}    [WARNING] This will completely destroy the target!")
    print(f"{R}    [ENTER] to launch nuclear attack → ", end="")
    input()

    print(f"\n{G}    ╔{'═'*62}╗")
    print(f"    {G}    ║                NUCLEAR ATTACK LAUNCHED!               ║")
    print(f"    {G}    ║           ALL METHODS + BYPASS ACTIVATED             ║")
    print(f"    {G}    ╚{'═'*62}╝{RESET}\n")

    t = threading.Thread(target=fake_logs, daemon=True)
    t.start()

    for i in range(int(duration), 0, -1):
        mins, secs = divmod(i, 60)
        status = random.choice(["DOWN", "CRITICAL", "OFFLINE", "FIREWALL DEAD"])
        print(f"   {R}[{W}TIMER{R}] {Y}{mins:02d}:{secs:02d} {R}| {G}Target: {status} {R}| {Y}Bypassing protections...")
        time.sleep(1)

    print(f"\n{R}    ╔{'═'*62}╗")
    print(f"    {R}    ║                ATTACK FINISHED!                       ║")
    print(f"    {R}    ║           TARGET SUCCESSFULLY ANNIHILATED            ║")
    print(f"    {R}    ╚{'═'*62}╝{RESET}\n")

    input(f"                       {W}Press Enter to return...{RESET}")

if __name__ == "__main__":
    run()
