from os import close, read, write
import requests
from colorama import Fore, Back, Style, init
init(convert=True)
def http():
    httpreq = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=all&country=all&anonymity=elite&ssl=all")
    http_file = open("http.txt", "w")
    http_file.write(str(httpreq.text))
    http_file.close()
def socks4():
    socks4req = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=all&country=all&anonymity=elite&ssl=all")
    socks4_file = open("socks4.txt", "w")
    socks4_file.write(str(socks4req.text))
    socks4_file.close()
def socks5():
    socks5req = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=all&country=all&anonymity=elite&ssl=all")
    socks5_file = open("socks5.txt", "w")
    socks5_file.write(str(socks5req.text))
    socks5_file.close()

socks5()
socks4()
http()
print(Fore.GREEN + "[+] Proxies Scraped! (Check the .txt Files)")
