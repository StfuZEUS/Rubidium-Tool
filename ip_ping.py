# option16_subdomain_scanner_real.py → 100% REAL SUBDOMAIN ENUMERATOR
import os
import time
import requests
import threading
import queue
import shutil
from datetime import datetime

R = "\033[91m"
W = "\033[97m"
G = "\033[92m"
Y = "\033[93m"
C = "\033[96m"
RESET = "\033[0m"

# Tera favorite red ping ASCII art (bilkul same)
PING_ART = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⡾⠟⠻⢶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠋⠉⠀⠀⠀⠀⠀⠙⠻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⢶⣤⡀⠀⠀⠀⠀⠀⠀⠙⠻⣦⣤⣤⡶⠾⠿⠶⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⠶⣦⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⡟⠁⠀⠀⠉⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠈⠻⢦⡀⠀⠀⠀⠀⠀⣾⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⠀⠀⠀⠀⠀⣀⣬⣿⣀⠀⠀⠀⠀⠛⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⢻⣦⣤⣰⣏⠁⠀⠙⠛⠻⢶⣴⣦⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡶⠟⠱⣏⠀⠀⠀⠀⠀⠈⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠈⠀⠀⠙⢳⡄⠀⠀⢀⣤⣼⣧⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⠋⠀⠀⠀⠀⠀⣿⣷⣤⣟⠁⠀⠉⠙⠻⢶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⢧⣤⣤⡀⠀⢀⣼⠋⣩⡟⣿⠆⠀⠀⠀⠀⠀⠉⣻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣾⠋⠉⠉⠉⠀⠛⣿⣀⣀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠏⠀⠀⣯⣉⣛⠛⠉⠁⠀⣏⠀⠻⠟⢳⣄⠀⠀⢀⣾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡿⠏⠁⠀⠀⢀⣠⣤⡀⠉⠉⣹⡧
⠀⠀⠀⠀⠀⠀⣤⣶⣦⣀⣤⡶⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣄⣤⣝⠛⣷⠀⠀⠀⠀⠀⠀⠈⠉⠛⠷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢴⡶⣦⠀⠀⠀⠀⢠⣶⣤⡾⠋⠀⠀⢀⣴⠶⠛⠁⢸⣇⣠⣤⣿⡆
⠀⠀⠀⠀⢠⡾⠋⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⠻⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠷⣦⣄⣠⣤⣤⣤⡀⠀⠀⠀⠀⠀⢠⣿⣰⣿⠀⠀⡀⠀⠈⣛⣿⣀⣤⣤⣤⠞⠁⢀⣴⣾⣿⠿⠋⠀⠉⠁
⠀⠀⠀⠀⠸⢷⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⢶⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠹⣧⠘⢷⣤⣤⣄⣀⢀⣀⡀⢘⣿⣩⣙⠷⠶⣶⠟⠛⠛⠛⠋⠉⠉⠀⠀⠀⢀⣴⡟⠀⠀⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠶⠋⠁⠀⣹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⠉⠙⠛⠙⠛⢻⣿⡟⠙⠿⠶⣿⣤⠤⣤⣀⡴⠖⢦⣀⠀⢠⣾⣷⣶⣦⡿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⢻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣋⣀⠀⠀⢠⣴⣋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡼⠇⠀⠀⠀⠀⠀⠀⠀⢀⣸⡟⠛⣷⡆⠀⣿⣤⣠⣤⣀⣤⣴⣦⣽⠇⣼⡿⠋⠀⣿⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⣷⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣄⡀⠀⠈⢩⡽⠃⠀⡿⢺⡝⠷⠶⠛⢷⣤⡴⠶⠶⣤⣀⡀⠀⣿⠁⠀⠀⠀⠀⢀⣀⡀⠀⢠⡟⢹⣷⣿⠋⠁⠀⠀⠉⠉⠈⠉⠁⢀⣿⡃⣰⡇⠀⠀⢰⡟⠀⠀⠀⠀⠀⠀⠀
⠀⣴⠟⠛⠻⠶⠛⠷⠟⠀⠀⠉⠙⠛⢶⡄⠀⠀⠀⢿⡂⢨⡟⢀⣤⣼⠀⠀⠀⢷⣄⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⣽⠖⠶⣤⡴⠶⠛⠉⠻⠞⠋⢀⣼⠛⠻⣷⡄⠀⠀⠀⠀⠀⢀⣶⠟⣋⡿⠋⠛⣿⠶⠿⠃⠀⠀⠀⠀⠀⠀⠀
⢸⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡀⠀⠀⣸⠇⠘⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡶⠶⠴⠟⠛⠻⣦⠀⠀⠀⠀⠀⣀⣤⣤⠶⠛⠁⠀⠀⢿⣄⠀⠀⠀⠀⠀⠈⣿⣰⡟⣿⠀⢀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠙⣻⣶⣟⣻⣷⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠷⣾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢛⣷⠀⠀⠀⠀⠘⢳⡄⠀⠀⠀⠻⠶⣦⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠈⠛⠃⢹⡇⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠸⣿⡛⠉⠉⠁⠀⠀⠀⠀⣤⣶⣄⠀⠀⠀⣴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠟⠁⠀⠀⠀⠀⣠⣿⣥⣤⡄⠀⢰⠶⣿⣷⡄⠀⢀⣀⠀⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠸⣷⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠙⠻⣦⡀⠀⠀⠀⠀⢰⡟⢸⡟⠀⠀⣶⣿⣧⣀⠀⠀⠀⠀⠀⣀⣤⠀⠀⠀⠀⢀⣀⠀⠀⠀⢰⡏⠀⠀⠀⠀⠀⠀⣼⠋⠀⠀⠀⠙⠓⠛⠀⠀⢉⣿⣦⡿⢻⣶⠾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⢿⣄⣀⣀⣠⡾⠃⢸⡇⠀⠀⡾⠋⠀⠉⠛⠛⠻⣆⣼⠋⠘⠷⠾⠋⠉⠉⠉⠛⠋⠻⣿⠁⠀⠀⠀⢀⣠⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⠛⠉⠉⠀⠀⠈⣿⢀⡴⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠟⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣀⡀⠀⠀⠀⢸⣇⠀⠀⢀⡴⢽⡧⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡗⠈⠙⠛⢛⡇⢠⣽⠇⠀⠀⢿⡄⠀⠀⠀⡀⠀⢀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠇⠀⠀⠀⠀⠘⠷⣾⣃⠀⠀⢀⣼⠃⣀⣴⠟⠉⠛⣫⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠞⠛⡏⠀⠀⠀⠀⠀⠀⠀⠀⠙⣧⣴⣟⣁⡾⠉⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⢠⡶⢤⡿⠁⠀⣰⠗⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⡟⠋⠉⠀⣠⣴⠾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡆⠀⢀⣤⠶⠖⠛⠀⠀⠀⠀⠀⡟⠀⠀⠀⠀⠀⢀⣀⣤⢤⡿⠉⠀⠀⠀⣼⠏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⡀⢸⡇⠀⠀⠀⠀⠀⠀⠀⢀⣻⡄⠀⣀⣤⡴⠟⠉⠀⠀⠀⢠⣴⠾⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡝⢿⡁⠀⠀⠀⠀⠀⠀⠀⣿⠋⠉⠉⠉⠀⠀⠀⠀⢠⡾⠻⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣾⠃⠀⠀⠀⠀⠀⠀⣴⠟⠀⠀⠀⠀⠀⠀⠀⠀⢿⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣆⠀⠀⠀⠀⠀⠀⠹⠶⣦⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡄⠀⠀⠀⠀⠀⠀⠘⠛⠛⢷⣄⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⡀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡿⢠⡴⠖⠒⠛⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠹⣦⠀⠀⠀⠀⠀⢸⡍⠉⠛⠋⠀⠀⠀⢀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⡉⠻⢦⣀⣀⣤⡼⠇⠀⠀⠀⠀⠀⢠⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡀⠘⢿⡉⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡀⠈⣇⡀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⠀⠉⣿⡄⠀⠀⠀⠀⢰⡟⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⣹⠇⠀⠀⣀⣀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣷⡀⣿⠀⠀⣼⠟⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣤⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

# Top 100 most common subdomains (real world)
WORDLIST = [
    "www","mail","ftp","webmail","cpanel","admin","test","dev","beta","staging",
    "api","app","shop","blog","forum","secure","login","portal","vpn","remote",
    "ns1","ns2","ns3","ns4","mx","smtp","pop","imap","webdisk","whm","autodiscover",
    "cms","store","mobile","m","demo","old","new","backup","db","mysql","sql",
    "server","cloud","panel","dashboard","client","clients","customer","customers",
    "support","help","ticket","tickets","billing","pay","payment","payments","invoice",
    "status","monitor","monitoring","stats","analytics","graph","report","reports",
    "git","repo","svn","docker","k8s","kubernetes","node","proxy","cdn","cache",
    "media","video","stream","live","radio","tv","news","press","events","event",
    "jobs","career","careers","team","about","contact","info","download","files",
    "share","upload","fileshare","drive","docs","doc","document","documents","wiki",
    "intranet","extranet","partner","partners","vendor","vendors","supplier","suppliers"
]

def check_subdomain(domain, subdomain, result_queue):
    full = f"{subdomain}.{domain}".strip(".")
    try:
        ip = socket.gethostbyname(full)
        result_queue.put((full, ip))
        print(f"    {G}[FOUND] {C}{full:<40} → {Y}{ip}")
    except:
        pass

def crtsh_search(domain, result_queue):
    try:
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            data = r.json()
            for entry in data:
                name = entry['name_value'].strip().lower()
                if domain in name and not name.startswith("*"):
                    if name not in [x[0] for x in result_queue.queue]:
                        result_queue.put((name, "crt.sh"))
                        print(f"    {G}[CRT.SH] {C}{name:<50} {Y}(Certificate)")
    except:
        pass

def run():
    os.system('clear')
    width = shutil.get_terminal_size().columns

    for line in PING_ART.strip().split('\n'):
        print(R + line.center(width) + RESET)
        time.sleep(0.02)

    print("\n" * 2)

    current_time = time.strftime("%H:%M:%S")
    print(f"      {W}[{W}{current_time}{W}] {W}[{R}>{W}] {W}Target Domain {R}:{W} ", end="")
    domain = input().strip().lower().replace("https://","").replace("http://","").split("/")[0]

    if not domain:
        print(f"{R}    [ERROR] Domain required!{RESET}")
        time.sleep(2)
        return

    print(f"\n{R}    [BRUTE] Starting real subdomain enumeration on {Y}{domain}{R}...{RESET}")
    time.sleep(1.5)

    found = queue.Queue()
    threads = []

    # Thread 1: crt.sh (passive recon)
    t1 = threading.Thread(target=crtsh_search, args=(domain, found))
    t1.start()
    threads.append(t1)

    # Thread 2+: Active brute-force
    for word in WORDLIST:
        full = word
        t = threading.Thread(target=check_subdomain, args=(domain, full, found))
        t.daemon = True
        t.start()
        threads.append(t)

    # Wait a bit
    time.sleep(8)
    for t in threads:
        t.join(timeout=0)

    total = found.qsize()

    if total == 0:
        print(f"    {R}[INFO] No subdomains found. Try manual wordlist or deeper scan.{RESET}")

    print(f"\n{Y}    [1]{W} Save Results    [2]{W} Scan Again    [0]{W} Back")
    print(f"\n    {W}Choose → ", end="")
    input()
    input(f"\n                       {W}Press Enter to return...{RESET}")

if __name__ == "__main__":
    import socket
    run()
