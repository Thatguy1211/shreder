import os, sys
import colorama
from colorama import *

init(convert=True)

def shred(folder, file, color_start, shred_level):
    if folder == True: #It's a folder
        for filename in os.listdir(file):
            file_path = os.path.join(file, filename)
            with open(file_path, "rb") as f:
                byte_list = list(f.read())
                if len(byte_list) > 0:
                    if shred_level == 3:
                        print(f"{color_start} {file_path} will be completely corrupted.")
                        num_bytes_to_corrupt = len(byte_list)
                    else:
                        percentage_corrupted = (shred_level+1)*25
                        print(f"{color_start} Corrupting {percentage_corrupted}% of {file_path}.")
                        num_bytes_to_corrupt = int(len(byte_list) * (shred_level/4.0))
                    for i in range(num_bytes_to_corrupt):
                        byte_list[i] = 0 #Corrupt the bytes by setting them to 0
                    with open(file_path, "wb") as f:
                        f.write(bytes(byte_list)) #Write the corrupted bytes back to the file
                    print(f"{color_start} Successfully corrupted {num_bytes_to_corrupt} bytes in {file_path}.")
                else:
                    print(f"{color_start} {file_path} is empty, skipping.")

    elif folder == False:#It's a file
        with open(file, "rb") as f:
            byte_list = list(f.read())
            if len(byte_list) > 0:
                num_bytes_to_corrupt = int(len(byte_list))
                percentage_corrupted = int(num_bytes_to_corrupt/len(byte_list) * 100)
                print(f"{color_start} Corrupting {percentage_corrupted}% of the file.")
                for i in range(num_bytes_to_corrupt):
                    byte_list[i] = 0 #Corrupt the bytes by setting them to 0
                with open(file, "wb") as f:
                    f.write(bytes(byte_list)) #Write the corrupted bytes back to the file
                    print(f"{color_start} Successfully corrupted {num_bytes_to_corrupt} bytes in the file.")
            else:
                print(f"{color_start} {file} is empty, skipping.")

def Main():
    print(f"{Fore.RED}\n\t\t\t  ██████  ██░ ██  ██▀███  ▓█████ ▓█████▄ ▓█████  ██▀███  \n\t\t\t▒██    ▒ ▓██░ ██▒▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒\n\t\t\t░ ▓██▄   ▒██▀▀██░▓██ ░▄█ ▒▒███   ░██   █▌▒███   ▓██ ░▄█ ▒\n\t\t\t  ▒   ██▒░▓█ ░██ ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄  \n\t\t\t▒██████▒▒░▓█▒░██▓░██▓ ▒██▒░▒████▒░▒████▓ ░▒████▒░██▓ ▒██▒\n\t\t\t▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░\n\t\t\t░ ░▒  ░ ░ ▒ ░▒░ ░  ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░\n\t\t\t░  ░  ░   ░  ░░ ░  ░░   ░    ░    ░ ░  ░    ░     ░░   ░ \n\t\t\t      ░   ░  ░  ░   ░        ░  ░   ░       ░  ░   ░     \n\t\t\t                                  ░                      \n")
    color_start = f"{Fore.RED}[{Fore.CYAN}+{Fore.RED}]{Fore.WHITE}"

    folder_choices = ['file', 'folder']

    shred_levels = [0,1,2,3]

    print(f"{color_start} Shreding levels:\n {Fore.CYAN}| \n{Fore.RED}[{Fore.CYAN}0{Fore.RED}]{Fore.WHITE} Weak\n{Fore.RED}[{Fore.CYAN}1{Fore.RED}]{Fore.WHITE} Medium\n{Fore.RED}[{Fore.CYAN}2{Fore.RED}]{Fore.WHITE} Strong\n{Fore.RED}[{Fore.CYAN}3{Fore.RED}]{Fore.WHITE} Completely gone")

    folder = input(f" {Fore.CYAN}| \n{color_start} Would you like to corrupt a folder or a singular file? [folder | file]\n").lower()
    if folder in folder_choices:
        if folder == 'file':
            file = input(f"{color_start} Where is the location of the singular file?\n")
            shred_level = int(input(f"{color_start} How much of the file would you like to be corrupted? [0-3]\n"))
            if shred_level in shred_levels:
                try:
                    shred(False, file, color_start, shred_level)
                except:
                    print(f"{color_start} Oooops! Looks like something went wrong, please make sure that what you were trying to corrupt was a real file, or that this program has ADMIN privileges")
        elif folder == 'folder':
            file = input(f"{color_start} Where is the location of the folder?\n")
            shred_level = int(input(f"{color_start} How much of the files in the folder would you like to be corrupted? [0-3]\n"))
            if shred_level in shred_levels:
                try:
                    for filename in os.listdir(file):
                        file_path = os.path.join(file, filename)
                    if os.path.isfile(file_path):
                        try:
                            shred(False, file_path, color_start, shred_level)
                        except:
                            print(f"{color_start} Oooops! Looks like something went wrong, please make sure that what you were trying to corrupt was a real file, or that this program has ADMIN privileges")
                    else:
                        print(f"{color_start} {filename} is not a file, skipping.")
                        print(f"{color_start} Successfully corrupted {shred_level}% of the files in the folder.")
                except:
                    print(f"{color_start} Oooops! Looks like something went wrong, please make sure that what you were trying to corrupt was a real file, or that this program has ADMIN privileges")

os.system('title Python digital Shreder / By that_guy1211 / Shreding files since 2023')
Main()
input()
