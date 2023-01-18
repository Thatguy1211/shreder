import os, sys
import colorama
from colorama import *

init(convert=True)

print(f'''{Fore.RED}

 ██▒   █▓ ██▓  ██████  █    ██  ▄▄▄       ██▓     ██▓▒███████▒▓█████  ██▀███  
▓██░   █▒▓██▒▒██    ▒  ██  ▓██▒▒████▄    ▓██▒    ▓██▒▒ ▒ ▒ ▄▀░▓█   ▀ ▓██ ▒ ██▒
 ▓██  █▒░▒██▒░ ▓██▄   ▓██  ▒██░▒██  ▀█▄  ▒██░    ▒██▒░ ▒ ▄▀▒░ ▒███   ▓██ ░▄█ ▒
  ▒██ █░░░██░  ▒   ██▒▓▓█  ░██░░██▄▄▄▄██ ▒██░    ░██░  ▄▀▒   ░▒▓█  ▄ ▒██▀▀█▄  
   ▒▀█░  ░██░▒██████▒▒▒▒█████▓  ▓█   ▓██▒░██████▒░██░▒███████▒░▒████▒░██▓ ▒██▒
   ░ ▐░  ░▓  ▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒  ▒▒   ▓▒█░░ ▒░▓  ░░▓  ░▒▒ ▓░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░
   ░ ░░   ▒ ░░ ░▒  ░ ░░░▒░ ░ ░   ▒   ▒▒ ░░ ░ ▒  ░ ▒ ░░░▒ ▒ ░ ▒ ░ ░  ░  ░▒ ░ ▒░
     ░░   ▒ ░░  ░  ░   ░░░ ░ ░   ░   ▒     ░ ░    ▒ ░░ ░ ░ ░ ░   ░     ░░   ░ 
      ░   ░        ░     ░           ░  ░    ░  ░ ░    ░ ░       ░  ░   ░     
     ░                                               ░                        
''')

os.system("title Byte Visualizer / By that_guy1211 / Visualizing bynary since 2023")

color = f"{Fore.RED}[{Fore.CYAN}+{Fore.RED}]{Fore.WHITE}"

print(f"{color} This program was designed to be used together with 'shreder.py' so please make sure you have it installed!")

file = input(f"{color} Location of the file to be visualized:\n")
try:
    with open(file, "rb") as f:
        for byte in f.read():
            print(f"{Fore.CYAN}{byte:08b} {Fore.RED}| ", end='')
except:
    print(f"{color} Oooops! Seems like something went wrong, please make sure the file you stated actually exists, and that this program has permission to view it")

input()