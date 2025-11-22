# option06.py - Useful Websites Vault
import os
import time
import shutil

R = "\033[91m"
W = "\033[97m"
RESET = "\033[0m"

SKULL = """
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡩⠙⢿⢯⣷⡄⠹⣇⡹⣿⣿⠛⣿⣿⡿⠣⢌⡾⢣⠝⢿⣿⣿⣃⠀⠀⠈⢉⣻⣿⠿⠛⣿⣿⣽⣿⣿⣿⡿⣿⣿⣿⠸⣶⢹⣏⡌⣼⡇⠘⢿⣿⣿⣿⣿⠓⣼⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡾⡆⢹⣿⣿⠆⠔⡰⢿⣿⣧⣜⢿⣴⡏⡟⣹⣿⣆⠀⣿⣯⡄⠑⢀⣰⣿⠟⢁⣴⡾⢛⣵⡿⢽⣿⠋⣰⣿⡟⢁⣆⣵⣾⣻⢸⣿⣿⣧⠈⣿⣿⣿⠟⠄⢹⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣟⡋⢁⣿⣶⢀⠹⣿⢁⠠⢡⣄⡩⢻⣻⡿⢟⡜⡕⡸⣿⣿⣇⠘⣿⣿⣾⣿⣿⣿⡐⠜⠿⡗⣨⢟⣶⢄⡨⡰⣿⣿⠁⣾⣿⢸⢹⡸⣺⣿⣿⣿⡆⢸⣿⣿⣶⣧⠁⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣼⣿⡿⢰⣾⣿⣿⢸⣆⠘⣾⠐⠌⣿⣿⠀⡏⢶⠻⣾⣿⡀⠂⢹⣿⣷⣿⣿⣿⣿⣿⣿⣿⠃⡐⣘⣯⢹⢅⡜⡵⠀⢸⡿⢘⣿⠻⡌⣾⡷⡝⣿⣿⣿⠁⣶⣝⡿⡫⢇⢇⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⢟⣭⢭⡿⣵⢸⣾⣿⣻⡄⢨⠀⢩⠺⣿⣻⠒⡿⢿⣇⢐⠄⠙⣿⡟⠻⣿⣿⣿⡟⢀⠄⢀⡾⣸⡇⡫⢾⠇⢡⢻⡇⡾⢋⣾⣷⢫⣶⡽⣸⣿⣿⠂⣿⡿⣟⢕⣣⣾⣿⣿⣿
⣿⡿⠿⠿⣿⣿⢏⡾⣽⣶⣽⡼⡇⣾⣿⣿⣿⣿⡄⢷⡕⣰⣆⡝⣧⣏⡚⣿⣇⣶⣬⣿⣿⣦⣸⣿⠏⢀⢀⣴⠟⣋⣸⡏⠄⡁⢐⣭⠆⢹⣇⣼⣿⣿⢸⣿⢇⢇⣿⣿⣷⣿⡣⢁⣾⣿⣿⣿⣿⣿
⣿⣿⡯⢐⡲⠵⣛⣼⣿⣿⣿⢹⠀⣿⣿⣿⣿⡿⣿⣾⣿⡦⡊⡳⢾⣿⣿⣿⡛⠿⣿⣿⣿⣿⣿⡟⠁⣴⣿⡵⠷⣳⡾⣱⡿⢁⠸⢛⡂⡿⢿⣿⣿⣿⡾⣿⢊⢾⣿⣿⡿⡵⣃⣽⣍⡻⣿⣿⣿⣿
⣿⣿⣷⣿⣿⣿⣿⣿⣿⡟⣵⢳⡇⣿⣿⢰⣿⡇⡛⣻⠿⢷⣽⣆⡀⢹⣷⣿⢿⢴⣿⣿⣿⣿⢻⣥⣼⣿⣿⡿⣼⣿⣟⠉⣢⣴⡿⠿⢛⣛⣷⣸⣟⣿⡇⣾⣧⣿⣿⢷⡾⣱⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣇⢿⡇⣿⣿⢸⣿⡻⢿⣿⣮⣄⡊⢙⡻⣶⣝⠻⢾⣷⡬⣱⣭⣿⡾⠿⣿⣿⣿⣿⡿⣫⠴⡛⢉⣡⣤⡶⢟⣛⣛⣻⣾⡟⡿⣷⡟⡜⣭⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡸⡞⡇⣿⣿⡨⡰⠶⢯⣝⡛⠽⡻⠷⣬⣐⢝⠳⣄⠙⢿⣜⡻⡿⢟⡽⣛⡿⢿⠟⡫⢑⣨⡶⣿⠿⣛⣩⡵⠶⠶⠦⡣⢧⢷⣿⢽⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⡿⡇⣿⢿⠀⣢⠭⣔⣚⠭⡓⢶⡅⠚⢝⡳⣬⡂⢕⠑⢿⡷⡔⡟⣼⠋⠐⢕⣨⢾⡫⢑⣩⠶⣛⡭⠖⢊⣩⡭⣅⢀⢿⢻⣿⣻⢏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣹⡇⣿⠠⣼⣷⡇⠀⠈⠙⠂⠕⡢⢄⡀⠈⢐⠽⢥⠑⣤⣭⢸⡇⢻⡏⡰⠏⠀⠁⢀⡠⠐⠉⠀⠂⠉⠐⠚⢿⣎⢧⢸⡌⢸⢣⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⣫⡷⠆⢹⣏⢿⣿⣧⣴⣤⣤⣀⠀⠀⠁⠈⠒⠄⡁⠊⢧⢻⣿⠘⢱⡟⡸⠃⠀⡠⠒⠁⠀⠀⠀⠀⣀⣠⣤⣄⣠⣿⢼⡆⡇⢸⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡑⢰⣽⣿⡇⢸⣏⠊⠻⡿⠿⢛⣋⣭⣭⣑⣒⠤⣄⣀⡈⠉⠉⠀⡙⠂⠁⠀⠌⠉⠡⣀⣀⣤⡴⠶⣛⣛⣉⡉⠛⠻⣿⠯⠚⣸⡇⣬⡣⡻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠃⣼⣿⣿⡇⢸⣿⡷⠦⠀⠀⢽⣟⣿⣿⣿⣿⣿⣶⣭⠙⢾⣥⢈⠀⢀⣄⠀⢀⠭⠂⠉⣩⣵⣶⣿⣿⣿⣿⣿⣦⠀⠀⠠⠾⢿⡇⡇⣷⣮⣑⡙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣇⣼⠟⠿⣟⢽⠘⣡⡴⠒⠠⠄⠙⠿⣿⣿⣿⣿⣿⣿⣿⠓⠀⠋⣀⣆⢻⣟⡄⠃⠀⠀⠐⣻⣻⣿⣿⣿⣿⡟⠉⢂⣡⠀⠶⣶⣤⠃⢧⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡿⢲⣿⣿⣣⡆⣿⠔⣪⣴⡾⢂⣠⣈⢭⣿⣯⣭⣭⢲⣶⣄⣰⣿⣿⢸⡇⣿⣦⣦⣠⣦⣭⣭⣛⢛⣛⣛⡁⠰⣶⣬⠑⢭⣮⢻⢣⢻⣍⢎⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⠿⢿⣿⣿⡟⠁⣼⣿⣿⣏⣷⢫⣾⣿⡏⣀⣭⣟⣻⣷⣭⣿⣿⣿⣤⡶⣽⣿⣿⣿⢸⡇⣿⣿⣿⡰⣶⣭⣿⣸⣿⣿⣷⣿⣤⡈⢇⣷⣄⠙⡦⢸⢸⣿⣷⣑⢝⡛⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡀⠈⠛⠏⠫⢘⣟⢿⣿⢣⡿⣎⢿⠹⠵⢿⣿⣿⣿⣿⣿⣟⣿⣿⣯⢱⣿⣿⣿⣿⣾⡇⣿⣿⣿⣧⣿⣿⢿⡿⠿⣿⣿⣿⣿⣿⣾⣿⣿⢱⠃⡿⣿⣿⣿⣿⣿⣮⣒⠍⠻⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⠧⡡⣂⣷⡽⣫⡆⢻⠈⢷⣄⠀⠀⠉⠉⠙⠛⠛⠛⠛⠋⠘⢛⠿⣿⣿⢻⡗⣿⣏⠿⡷⠌⠑⠻⠿⠿⠟⠛⠛⠛⠛⠋⠁⡠⠋⣸⠕⢿⣿⣿⣿⣿⣿⣿⣷⠀⣈⠙⣿⣿⣿⣿
⣿⣿⣿⡿⠟⠛⠐⣴⣿⣬⡐⠟⢁⣥⢸⣇⢠⡍⠁⠀⠀⠀⠀⠀⠀⠀⢀⡀⢰⣿⢃⣿⡟⢼⣷⢹⣿⣜⣿⡄⣀⠀⠀⠂⠀⠀⠀⠀⠄⠄⠀⠰⢀⡏⣿⣆⠙⢿⣿⣿⣿⣿⣿⣼⣾⣔⣿⣿⣿⣿
⣿⣿⠏⢀⣼⣷⣾⣿⣿⣿⣿⣿⣿⣿⣇⡿⡄⢣⠐⡀⢀⠀⠀⣤⣶⣾⣿⣷⡌⠉⠹⠻⠁⠨⠭⠋⠿⠛⠉⣰⠟⣹⣶⣦⣤⠄⡀⠀⡰⡀⢠⠃⣼⡟⣼⣿⣷⡄⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⢧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢰⢹⡈⠆⠙⢆⢪⣢⠈⣿⣿⣿⣿⣿⣦⠀⠀⠲⠂⠀⠀⠀⢀⣴⣥⣾⣿⣿⡿⢃⢜⠂⡔⡐⢀⠆⢰⣿⡳⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⡞⣾⣷⡸⡄⠡⠠⡙⡍⢔⣚⡭⠝⣛⣻⡆⠔⠀⠀⠀⠀⢄⠿⣿⣛⡛⠫⠭⠑⡡⢁⠞⡐⠀⠌⡌⣼⢯⡝⡌⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣷⣿⣿⣿⣿⣿⣿⡿⣿⠟⠛⠋⠥⢺⠛⣼⣿⣷⡱⡙⡄⠑⡘⢌⠓⡲⠭⣟⣑⠲⠀⠀⠀⠀⠀⠀⠀⢉⣀⣀⣀⡭⠭⠞⣠⢊⠌⢀⢈⠞⣼⡿⣐⣷⠑⢝⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣥⠀⣠⣴⣿⡿⡫⢎⣼⣿⣿⣿⣷⡝⡜⠄⠘⢄⠢⡈⠶⣄⣈⠙⠙⠉⠿⠿⠿⠿⠿⠿⠿⢉⣀⠄⢀⡴⠁⠂⠰⢢⢊⣾⣿⣿⡻⡏⡎⣦⣈⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣃⣼⣿⣿⣿⡌⡘⣿⣿⣿⣿⣿⣿⣿⡜⢌⢆⠈⢂⠙⢰⡌⠛⠻⠿⠶⠄⠀⠤⠶⠾⠯⠿⠛⠁⡄⠌⡔⠁⣰⡷⣡⣿⣿⣿⣿⠋⣠⣌⢢⢹⣄⡹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠷⢡⠹⣿⣿⣿⣿⣿⣿⣿⣎⣦⠣⡁⡁⠜⠇⠀⠀⠀⠀⠠⠄⠀⡔⠀⠀⠀⣠⣾⠁⠊⠐⣴⢏⣼⣿⣿⣿⣿⣧⢀⣿⣿⣮⠠⡡⣱⡄⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣴⠆⢡⣿⣿⣿⣿⣿⣿⣿⣿⡿⡅⢻⣿⣆⠀⠀⠀⠀⠀⡘⠀⠐⣱⢀⣤⣾⣿⠃⣡⣠⡾⢣⢂⣿⣿⣿⣿⣿⣯⣠⣿⣿⣿⣿⠔⢹⣧⡑⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢀⣾⣿⣿⣿⣿⣿⣿⠿⠛⠐⡕⣷⡙⢿⣷⠀⠀⠀⠀⠇⠀⠀⠸⣼⣿⣿⣧⣾⠿⢏⣴⣿⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⠃⡀⠸⣿⣿⣿⣿⣿⡿⠛⠋⣠⣦⢣⢻⣿⣦⡹⠀⠀⠀⠀⣰⠀⠀⡇⣿⣿⣿⠟⠁⣠⣿⣿⣿⣌⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣏⣁⡁⢱⣤⣽⣿⣿⣿⣿⣿⠁⣼⣿⣿⣬⢪⢻⣿⣿⣦⡀⠀⠀⠉⡄⢰⠹⠛⠉⠀⣠⣾⣿⢟⡴⠵⣋⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⡇⠧⣿⣿⣿⣿⣿⣦⣄⣀⠃⡘⣀⣠⣴⣿⣿⣿⡇⡌⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠱⡙⢿⣿⣿⣿⣿⣿⣿⡸⢧⣿⣿⣿⣿⣿⢟⡫⢓⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿
⣇⠀⠙⢿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⢞⢮⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢋⣵⣿⢱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⠿⢻
⣿⣄⣁⣼⣷⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣷⢹⢼⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣯⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣴⣾
"""

websites = [
    "boredhumans.com", "pointerpointer.com", "quickdraw.withgoogle.com", "10minutemail.com",
    "hackertyper.net", "longdogechallenge.com", "cat-bounce.com", "zoomquilt.org",
    "omfgdogs.com", "thisissand.com", "staggeringbeauty.com", "remove.bg",
    "heropatterns.com", "radio.garden", "scaleofuniverse.com", "futureme.org",
    "geoguessr.com", "riddle.com", "wordwall.net", "scratch.mit.edu",
    "github.com", "stackoverflow.com", "codepen.io", "w3schools.com",
    "regex101.com", "canva.com", "tinyurl.com", "virustotal.com",
    "privnote.com", "pastebin.com", "jsonformatter.org", "temp-mail.org",
    "builtwith.com", "archive.org", "namecheap.com", "coolors.co",
    "photopea.com", "unsplash.com", "pixabay.com", "pimeyes.com",
    "coursera.org", "edx.org", "khanacademy.org", "mitocw.edu",
    "ted.com", "britannica.com", "readthedocs.io", "geeksforgeeks.org",
    "freecodecamp.org", "codecademy.com", "cloudflare.com", "owasp.org",
    "developer.mozilla.org", "howstuffworks.com", "space.com", "livescience.com",
    "softschools.com", "nasa.gov", "nationalgeographic.com", "sciencealert.com",
    "bbc.com", "reuters.com", "bloomberg.com", "techcrunch.com",
    "theverge.com", "wired.com", "cnn.com", "aljazeera.com",
    "ndtv.com", "geo.tv", "dawn.com", "dailypakistan.com.pk",
    "tribune.com.pk", "express.pk", "time.com", "fortune.com",
    "forbes.com", "vice.com", "medium.com", "quora.com",
    "spotify.com", "soundcloud.com", "netflix.com", "primevideo.com",
    "crunchyroll.com", "twitch.tv", "discord.com", "pinterest.com",
    "instagram.com", "twitter.com", "facebook.com", "snapchat.com",
    "reddit.com", "tiktok.com", "imdb.com", "letterboxd.com",
    "yahoo.com", "outlook.com", "protonmail.com", "speedtest.net"
]

def run():
    os.system('clear')
    time.sleep(0.8)

    width = shutil.get_terminal_size().columns

    # RED SKULL ART
    for line in SKULL.strip().split('\n'):
        print(R + line.center(width) + RESET)
        time.sleep(0.05)

    print("\n" * 2)
    print(R + " " * ((width - 50) // 2) + "╔" + "═" * 48 + "╗")
    print(R + " " * ((width - 50) // 2) + "║" + W + "        UNDERGROUND USEFUL WEBSITES VAULT       " + R + "║")
    print(R + " " * ((width - 50) // 2) + "╚" + "═" * 48 + "╝" + RESET)
    print("\n" * 2)

    # Websites list - slow print
    for site in websites:
        print(f"      [{R}+]{W} {site}")
        time.sleep(0.06)

    print("\n" * 3)
    input(f"                       {W}Press Enter to go back...{RESET}")

if __name__ == "__main__":
    run()
