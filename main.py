# main.py - Rubidium Tool (All files in same folder - Pro Version)
import os
import importlib
import shutil

R = "\033[91m"
W = "\033[97m"
RESET = "\033[0m"

BANNER = """
 ██▀███   █    ██  ▄▄▄▄    ██▓▓█████▄  ██▓ █    ██  ███▄ ▄███▓   
▓██ ▒ ██▒ ██  ▓██▒▓█████▄ ▓██▒▒██▀ ██▌▓██▒ ██  ▓██▒▓██▒▀█▀ ██▒   
▓██ ░▄█ ▒▓██  ▒██░▒██▒ ▄██▒██▒░██   █▌▒██▒▓██  ▒██░▓██    ▓██░   
▒██▀▀█▄  ▓▓█  ░██░▒██░█▀  ░██░░▓█▄   ▌░██░▓▓█  ░██░▒██    ▒██    
░██▓ ▒██▒▒▒█████▓ ░▓█  ▀█▓░██░░▒████▓ ░██░▒▒█████▓ ▒██▒   ░██▒   
░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒ ░▒▓███▀▒░▓   ▒▒▓  ▒ ░▓  ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░   
  ░▒ ░ ▒░░░▒░ ░ ░ ▒░▒   ░  ▒ ░ ░ ▒  ▒  ▒ ░░░▒░ ░ ░ ░  ░      ░   
  ░░   ░  ░░░ ░ ░  ░    ░  ▒ ░ ░ ░  ░  ▒ ░ ░░░ ░ ░ ░      ░      
   ░        ░      ░       ░     � suflet     ░     ░            ░      
                        ░      ░                                 
"""

def clear():
    os.system('clear')

def banner():
    clear()
    width = shutil.get_terminal_size().columns
    gradient = ["\033[38;2;139;0;0m","\033[38;2;160;0;0m","\033[38;2;179;0;0m",
                "\033[38;2;197;0;0m","\033[38;2;216;0;0m","\033[38;2;255;0;0m"]
    for i, line in enumerate(BANNER.strip().split('\n')):
        print(gradient[i % 6] + line.center(width) + RESET)
    print("\n\n")
    print(W + "github.com/StfuZEUS/Rubidium-Tool".center(width) + RESET)
    print("\n\n")

def run_tool(module_name):
    try:
        module = importlib.import_module(module_name)
        if hasattr(module, "run"):
            module.run()
        else:
            print(f"{R}[!] {module_name}.py mein 'run()' function nahi hai bhai!")
    except ImportError:
        print(f"{R}[!] {module_name}.py file nahi mili!")
    except Exception as e:
        print(f"{R}[!] Error: {e}")
    
    input(f"\n{W}Press Enter to continue...{RESET}")
    show_menu()

def show_menu():
    banner()

    left = ["Tool Info","Tool Site","Virus Builder","Sql Vulnerability",
            "Website Scanner","illegal Website","Search In DataBase",
            "Dox Creater","Dox Attacker","Username Tracker"]
    right = ["Email Tracker","Email Info","Number Info","Ip Info",
             "Ip Port Scanner","Ip Ping","Ip Generator",
             "Password Encrypted","Password Decrypted","Get Your Ip"]

    left_lines = [f"{W}[{R}{i+1:02d}{W}] {R}->{RESET} {W}{name}{RESET}" for i, name in enumerate(left)]
    max_left = max(len(l) for l in left_lines)

    for i in range(10):
        print(left_lines[i].ljust(max_left) + "        " + f"{W}[{R}{i+11:02d}{W}] {R}->{RESET} {W}{right[i]}{RESET}")

    print(f"\n{R}╭───({W}Rubidium{R})-{W}~{R}")
    print(f"╰${W} »{R} ", end="")

    choice = input("").strip()

    if choice in ["0", "exit", "quit"]:
        print(f"{W}Bye Bhai! Rubidium Off!{RESET}")
        exit()

    tools = {
        "1": "tool_info",           "01": "tool_info",
        "2": "tool_site",           "02": "tool_site",
        "3": "virus_builder",       "03": "virus_builder",
        "4": "sql_vulnerability",   "04": "sql_vulnerability",
        "5": "website_scanner",     "05": "website_scanner",
        "6": "illegal_website",     "06": "illegal_website",
        "7": "search_database",     "07": "search_database",
        "8": "dox_creater",         "08": "dox_creater",
        "9": "dox_attacker",        "09": "dox_attacker",
        "10": "username_tracker",   "10": "username_tracker",
        "11": "email_tracker",      "12": "email_info",
        "13": "number_info",        "14": "ip_info",
        "15": "ip_port_scanner",    "16": "ip_ping",
        "17": "ip_generator",       "18": "password_encrypted",
        "19": "password_decrypted", "20": "get_your_ip"
    }

    if choice in tools:
        run_tool(tools[choice])
    else:
        print(f"{R}[!] Galat number daala bhai! 01-20 try kar!")
        input(f"{W}Enter dabao wapas jaane ke liye...{RESET}")
        show_menu()

if __name__ == "__main__":
    show_menu()
