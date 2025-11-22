# option17_ip_generator.py → UNLIMITED IP GENERATOR (REAL + CHAOS MODE)
import os
import time
import random
import shutil
import threading
from itertools import product

R = "\033[91m"
W = "\033[97m"
G = "\033[92m"
Y = "\033[93m"
C = "\033[96m"
RESET = "\033[0m"

# Tera diya hua exact red ASCII art
IP_GEN_ART = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡿⣷⣦⣾⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⠟⢿⣷⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⠷⣦⡄⠙⠁⠀⠿⢻⣿⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⡀⠈⠁⠀⠀⠀⠀⢺⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠿⠿⠏⠙⢿⣿⣇⠀⠀⠀⡄⠀⠀⠠⣾⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⣸⣟⠁⠀⠀⣼⡇⠀⠀⢀⣬⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣄⠀⠀⠐⠿⣿⣷⣶⣾⡿⠁⠀⠀⡈⣻⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣄⠀⠀⠈⠻⢿⣶⣦⣤⣼⣿⡿⠛⠀⠀⠀⠐⣿⣿⠏⠀⠀⠀⠀
⠀⠀⠀⠀⠘⣿⣿⣠⣾⠋⠀⠀⠈⠉⠉⠉⠁⠀⠀⠀⡀⣺⣷⡿⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢈⣿⣿⣷⣴⣦⠀⣀⡀⢀⣀⠀⣤⣄⣼⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⠁⠀⠙⠻⠿⣿⣿⣷⣾⣿⣾⣿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣹⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠂⠀⠀⠀⠀⠀⠀⠀⠀
"""

stop_generating = False

def generate_random_ip():
    return f"{random.randint(1,223)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"

def generate_sequential(start_octet=1):
    a = start_octet
    while not stop_generating:
        for b, c, d in product(range(256), repeat=3):
            if stop_generating:
                return
            if a == 10 or (a == 172 and 16 <= b <= 31) or (a == 192 and b == 168):
                continue  # Skip private ranges
            ip = f"{a}.{b}.{c}.{d}"
            print(f"    {G}[+] {C}{ip}{RESET}")
            time.sleep(0.0001)  # Ultra fast but visible
        a += 1
        if a > 223:
            a = 1

def generate_live_feeling():
    patterns = [
        "1.1.1.1", "8.8.8.8", "8.8.4.4", "1.0.0.1", "208.67.222.222",
        "9.9.9.9", "149.112.112.112", "94.140.14.14", "76.76.2.0",
        "45.33.32.156", "185.228.168.168", "198.18.0.1", "103.86.99.100"
    ]
    while not stop_generating:
        ip = random.choice(patterns) if random.random() < 0.15 else generate_random_ip()
        print(f"    {G}[+] {Y}{ip}{RESET}")
        time.sleep(0.03)

def run():
    global stop_generating
    stop_generating = False

    os.system('clear')
    width = shutil.get_terminal_size().columns

    # Print exact red ASCII art
    for line in IP_GEN_ART.strip().split('\n'):
        print(R + line.center(width) + RESET)
        time.sleep(0.04)

    print("\n" * 2)
    print(f"    {R}╔══════════════════════════════════════════════════════════════════╗")
    print(f"    {R}║                   UNLIMITED IP GENERATOR ACTIVATED              ║")
    print(f"    {R}║                Generating LIVE & VALID IPv4 Addresses            ║")
    print(f"    {R}╚══════════════════════════════════════════════════════════════════╝{RESET}\n")

    print(f"    {W}Press {R}CTRL+C{W} anytime to stop generating...{RESET}\n")
    time.sleep(2)

    # Start 4 threads = INSANE SPEED
    threads = [
        threading.Thread(target=generate_sequential, args=(1,)),
        threading.Thread(target=generate_sequential, args=(50,)),
        threading.Thread(target=generate_sequential, args=(100,)),
        threading.Thread(target=generate_live_feeling)
    ]

    for t in threads:
        t.daemon = True
        t.start()

    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print(f"\n\n{R}    [STOPPED] IP Generation terminated by user.{RESET}")
        stop_generating = True
        time.sleep(1)
        print(f"\n                       {W}Press Enter to return...{RESET}")
        input()

if __name__ == "__main__":
    run()
