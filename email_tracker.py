# option11_email_tracker.py - ULTIMATE EMAIL TRACKER + INBOX SPY
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

EMAIL_ART = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡙⠛⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣜⣛⡛⢻⡖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡼⠛⠛⠛⠋⢻⡔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣾⣶⠶⠶⠿⠿⣶⢿⡳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡼⣢⣀⢀⣀⣀⢀⣠⡀⢻⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣼⠛⠉⠉⠉⠉⠁⠈⠉⠋⠛⢧⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠼⠥⠦⢡⡶⠶⠄⠖⠂⠶⣤⢞⣧⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣀⣠⣄⢀⣀⣀⣀⣄⢀⣤⡀⢀⡙⡛⢆⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⢞⣟⣩⣭⠉⠈⠋⠉⠈⢉⠈⠉⠉⠚⠛⢣⣼⣆⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠟⢛⣭⣬⣤⡤⠴⠶⠢⠗⠟⠃⠾⠷⠆⣴⣤⡌⠙⣎⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢸⢿⣞⣟⣩⣥⣶⣶⣿⣾⣴⣖⣷⣤⣤⣤⡴⠄⠉⠰⠷⣿⡔⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣔⣿⣿⣽⣿⣿⣿⣿⡿⠿⠟⣟⣻⠿⠿⠞⢻⣛⣳⣚⣽⣧⣤⡼⡔⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣔⣿⣾⣿⣿⣯⣅⠉⠀⠤⠂⠀⢀⠀⠀⢀⠚⡉⠀⢁⡻⢗⢒⡚⣿⣯⡠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢔⣀⣿⢿⣚⣤⢽⣦⣀⡤⠤⠧⠖⠰⠒⡶⠷⣦⣴⡴⠋⠐⣀⣸⡍⢫⢿⣷⡢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⢺⣯⣭⣘⢛⡿⠾⣛⡍⠁⠂⠐⠐⠀⠐⠇⠦⠭⣽⣷⢦⣶⡛⠹⣧⣬⡾⠛⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣨⡞⣿⣧⣼⢛⠩⠴⠂⠁⠀⠀⠀⠀⡀⠐⠀⠀⠤⠄⡈⢙⡛⠯⣿⣯⣅⣬⡿⠿⣯⣧⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣛⣿⡿⢟⡅⢀⣆⣀⣴⣶⣾⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⣮⡻⠶⣏⡻⢿⣧⣽⠿⣿⣿⡇⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⡟⢋⣀⣦⣾⣿⠿⣿⣿⣿⡿⠉⢩⣽⢿⣿⣿⣿⡟⣿⣿⡿⢿⣷⣬⡻⣮⣁⣷⣴⢾⣛⣻⡄⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣸⠿⢋⣠⣬⣿⣿⣿⣿⡛⢿⣿⣿⣿⣀⡈⠁⣾⣻⣿⣿⢷⣿⣿⡟⠶⣟⢻⣷⣦⣙⣯⣿⣿⣟⣻⣾⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣿⢢⣾⣿⣿⣿⡏⡇⠸⡇⢸⣿⣿⢮⣿⣷⣿⣿⣿⠟⢃⣾⣿⣿⠣⣼⠋⣿⣿⣿⣿⣯⣿⣿⠟⣻⣶⣿⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣴⠷⢝⣆⠛⢿⢿⡧⡷⢻⡆⢳⡀⢻⣟⡿⣿⣛⣻⣚⣋⣠⡿⣿⣾⠇⡰⠋⢠⣯⣿⠿⢻⣽⣋⣿⣿⣟⣭⣙⣹⣏⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡴⣷⣦⢀⣘⠳⠓⠈⠤⠙⠳⠱⢀⠳⣀⠈⠛⠿⢿⢯⠽⠵⠾⠛⠋⢠⡔⠁⠤⠍⢋⣼⡷⣿⣵⢿⣿⢷⡚⠛⢿⣭⣹⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣽⣅⣀⠹⠿⡉⠁⠶⠶⠀⣀⠁⠀⠀⠀⣀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⡀⣩⣤⡴⣚⡿⠷⣟⡩⠟⠋⢀⣠⡽⢳⣾⣾⠟⠻⡁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣵⣈⠉⢿⣜⠋⠙⠓⠂⣄⡀⠈⠁⠐⠂⠠⡍⢈⡘⠒⠘⠒⢒⠓⢛⡃⢉⣡⠰⠒⠊⣁⣈⣥⠴⠂⠛⠛⢤⣄⣒⣠⣠⣩⣴⣷⠿⡅⠀⠀⠀⠀
⠀⠀⠀⢀⣙⣙⢿⣼⠛⠛⢷⣤⠆⢀⣀⠀⠙⠛⠰⠶⠤⠤⣤⣤⣤⣥⣤⣤⣤⠤⢤⡶⠷⠖⠛⠙⣉⣉⣤⣤⡦⠶⢖⠚⠋⠙⢧⣭⠁⠀⠙⡿⢻⠢⠀⠀⠀
⠀⠀⠠⣽⣿⡛⠛⠿⢶⣠⣤⡝⠃⡈⠉⠀⠓⠚⠷⠶⠴⢴⠤⠤⢴⣤⡤⠤⠤⡴⠤⠶⠖⠲⠚⠋⠉⢉⠁⢀⣀⣀⣾⣿⣦⣤⠴⠾⠿⠿⣿⡛⠛⢷⢀⠀⠀
⠀⠀⣽⡟⠻⣳⣴⡄⢤⣭⠷⠀⠙⠙⠐⠶⠆⢠⣄⠈⠉⠀⠶⠂⠠⠔⠀⠰⠴⠀⠺⠓⠂⠰⠾⠂⠚⢻⠇⠈⠉⠱⢄⢀⣀⣬⡙⢦⣦⣶⠿⡿⠷⣿⣧⢄⠀
⠐⠉⠛⠉⠛⠃⠈⠋⠀⠀⠉⠋⠁⠘⠋⠀⠚⠁⠀⠐⠛⠃⠀⠋⠁⠐⠂⠐⠂⠘⠁⠀⠋⠃⠐⠛⠓⠘⠛⠋⠘⠛⠋⠈⠉⠀⠀⠀⠙⠋⠉⠛⠛⠛⠛⠁⠂
"""

def run():
    os.system('clear')
    time.sleep(0.9)
    width = shutil.get_terminal_size().columns

    # Red ASCII Art
    for line in EMAIL_ART.strip().split('\n'):
        print(R + line.center(width) + RESET)
        time.sleep(0.05)

    print("\n" * 2)

    # Input fields with time
    current_time = time.strftime("%H:%M:%S")
    print(f"      {W}[{W}{current_time}{W}] {W}[{R}>{W}] {W}Your Email         : {W}", end="")
    your_email = input().strip()

    print(f"      {W}[{W}{current_time}{W}] {W}[{R}>{W}] {W}Email Password     : {W}", end="")
    password = input().strip()

    print(f"      {W}[{W}{current_time}{W}] {W}[{R}>{W}] {W}Sender Email       : {W}", end="")
    target_email = input().strip()

    if not all([your_email, password, target_email]):
        print(f"\n      {R}[-] All fields required! Aborting...{RESET}")
        time.sleep(2)
        return

    print(f"\n{R}    [CONNECTING] Establishing secure SMTP/IMAP tunnel...{RESET}")
    time.sleep(2.5)
    print(f"{R}    [AUTH] Logging into {your_email} via encrypted channel...{RESET}")
    time.sleep(2)

    print(f"{G}    [+] Authentication Successful!{RESET}")
    print(f"{R}    [SCAN] Searching all mailboxes for emails from/to {Y}{target_email}{RESET}")
    time.sleep(3.5)

    # Fake inbox results
    print(f"\n{G}    ╔{'═'*68}╗")
    print(f"    {G}    ║               EMAIL TRACKING RESULTS FOUND!                ║")
    print(f"    {G}    ╚{'═'*68}╝{RESET}\n")

    emails_found = random.randint(5, 18)
    subjects = ["Payment Received", "Urgent: Action Required", "Login from new device", "Your Amazon Order", "Bank Alert", "Meeting Tomorrow", "I miss you", "Password Reset", "Invoice #7865", "Photo attached", "Check this out"]

    for i in range(emails_found):
        subject = random.choice(subjects)
        date = time.strftime("%d %b %Y", time.localtime(time.time() - random.randint(10000, 900000)))
        direction = random.choice(["Sent →", "Received ←"])
        print(f"    {R}[{G}{i+1}{R}] {W}{direction} {C}{target_email}")
        print(f"        {Y}Subject : {subject}")
        print(f"        {Y}Date    : {date}")
        print(f"        {Y}Size    : {random.randint(10, 890)} KB")
        print(f"        {Y}Status  : {'Read' if random.random() < 0.6 else 'Unread'}\n")
        time.sleep(0.4)

    print(f"{R}    [SUMMARY] Total {G}{emails_found}{R} emails found between you and {Y}{target_email}")
    print(f"{R}    [WARNING] Full conversation history has been tracked!")

    print(f"\n{Y}    Options:")
    print(f"    {W}[1]{R} Download all emails as .eml")
    print(f"    {W}[2]{R} Export to PDF report")
    print(f"    {W}[3]{R} Forward all to another email")
    print(f"    {W}[0]{R} Exit")

    print(f"\n    {W}Choose → ", end="")
    input()

    print(f"\n" * 2)
    input(f"                       {W}Press Enter to return...{RESET}")

if __name__ == "__main__":
    run()
