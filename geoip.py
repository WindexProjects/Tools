import requests
from colorama import Fore, Back, Style, init 
init(convert=true)
geoip = input("Enter IP Address: ")
geolocate = requests.get("https://extreme-ip-lookup.com/json/" + str(geoip))
if (geolocate.status_code == 404):
    print(Fore.RED + "[-] Could Not Geolocate, (Error 404)..")
if (geolocate.status_code == 200):
    print(Fore.GREEN + "[+] Geolocating Successful!")
    print(geolocate.text)
else:
    print(Fore.YELLOW + "[?] Error Code: ", geolocate.status_code, "Could not Geolocate!")
   #May Add support for saving the Results in a .txt file later :)
