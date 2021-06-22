import requests
from colorama import Fore, Back, Style, init
init(convert=True)
print(Fore.YELLOW + "█     █░▓█████  ▄▄▄▄    ██░ ██  ▒█████   ▒█████   ██ ▄█▀     █████▒█    ██  ▄████▄   ██ ▄█▀▓█████  ██▀███")
print(Fore.GREEN + "▓█░ █ ░█░▓█   ▀ ▓█████▄ ▓██░ ██▒▒██▒  ██▒▒██▒  ██▒ ██▄█▒    ▓██   ▒ ██  ▓██▒▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒")
print(Fore.RED + "▒█░ █ ░█ ▒███   ▒██▒ ▄██▒██▀▀██░▒██░  ██▒▒██░  ██▒▓███▄░    ▒████ ░▓██  ▒██░▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒")
print(Fore.MAGENTA+"░█░ █ ░█ ▒▓█  ▄ ▒██░█▀  ░▓█ ░██ ▒██   ██░▒██   ██░▓██ █▄    ░▓█▒  ░▓▓█  ░██░▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  ")
print(Fore.BLUE + "░░██▒██▓ ░▒████▒░▓█  ▀█▓░▓█▒░██▓░ ████▓▒░░ ████▓▒░▒██▒ █▄   ░▒█░   ▒▒█████▓ ▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒")
print(Fore.YELLOW + "░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒    ▒ ░   ░▒▓▒ ▒ ▒ ░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░")
print(Fore.GREEN + "  ▒ ░ ░   ░ ░  ░▒░▒   ░  ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░    ░     ░░▒░ ░ ░   ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░")
print(Fore.RED + "  ░   ░     ░    ░    ░  ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░     ░ ░    ░░░ ░ ░ ░        ░ ░░ ░    ░     ░░   ░ ")
print(Fore.MAGENTA + "    ░       ░  ░ ░       ░  ░  ░    ░ ░      ░ ░  ░  ░                ░     ░ ░      ░  ░      ░  ░   ░     ")
print(Fore.BLUE + "                      ░                                                     ░                               ")
print(Fore.RED + " ")
webhook = input("Enter Webhook: ") #Only works for discord webhooks
spam = input("Enter amount to Spam: ")
message = input("Message to Spam: ")
for x in range (int(spam)):
    post = requests.post(webhook, json={'content' : message})
    if (post.status_code == 204):
        print(Fore.GREEN + "[+] Message Sent! ")
    elif (post.status_code == 429):
        print(Fore.RED + "[-] Failed to Send! ")
    else:
        print(Fore.YELLOW + "[x] Possible Error! Message May not've sent!")
