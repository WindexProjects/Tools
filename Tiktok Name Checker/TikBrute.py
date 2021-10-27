import httpx, subprocess, asyncio, time, threading, platform
from webhook import webhook as wb
from colorama import Fore, Style, init
if platform.uname().system.lower() != 'windows':
	print("Operating System Not Supported! Requires Windows.")
	time.sleep(3)
	quit()
webhook = ' ' #Webhook Goes Here, if you'd like to use a webhook.
init(convert=True)
g = Fore.GREEN
r = Fore.RED
y = Fore.YELLOW
def total():
	tot = 0
	with open('usernames.txt','r') as s:
		tot += len(s.readlines())
	return tot
def good(name):
	with open('good.txt','a') as s:
		s.write(f"{name}\n")

def bad(name):
	with open('bad.txt','a') as s:
		s.write(f"{name}\n")

def error(name, code):
	with open('errored.txt','a') as s:
		s.write(f"NAME: {name}, CODE: {code}\n")
def gather_(client):
	print(f"{g}[+] Loading Names...")
	tasks = list()
	headers = {
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0"
	}
	with open('usernames.txt','r') as usernames:
		for x in usernames.readlines():
			tasks.append(client.get(f'https://www.tiktok.com/@{x.rstrip()}?', allow_redirects=False, headers=headers))
			subprocess.call(f"title [!] LOADED {len(tasks)}/ {total()} NAMES[!] ----- TikTok Username Checker... Made by Windex \u2664", shell=True)
	subprocess.call("cls")
	print(f"{Fore.RESET}Loaded {len(tasks)}, Beginning to Check.. \nTime May Vary Depending on Amount of Usernames!")
	return tasks
async def req():
	async with httpx.AsyncClient(timeout=None) as client:
		tt = time.time()
		tasks = gather_(client)
		res = await asyncio.gather(*tasks)
		gd, bd, rl,err = 0, 0, 0,0
		for x in res:
			name = str(x.url).split('@')
			name = name[1][:len(name[1])-1]
			match x.status_code:
				case 200:
					print(f"{r}[-] TAKEN NAME: {Fore.RESET}@{name}")
					bad(name)
					bd += 1
					#subprocess.call(gz, shell=True)
				case 404:
					print(f"{g}[+] AVAILABLE / BANNED: {Fore.RESET}@{name}")
					good(name)
					gd += 1
					#subprocess.call(gz, shell=True)
				case 429:
					error(name, code=x.status_code)
					err += 1
					#subprocess.call(gz, shell=True)
				case 403:
					error(name, code=x.status_code)
					rl += 1
					#subprocess.call(gz, shell=True)
		ttt=time.time()
		gz = f"title GOOD: {gd} BAD: {bd} RATELIMITED: {rl} ERRORED: {err}"
		wb(good=gd, bad=bd, r=rl, webhook=webhook, amt=total(), t=tt, tt=ttt)
		subprocess.call(gz, shell=True)
asyncio.run(req())
Fore.RESET
print("Press any key to Close..", end='')
subprocess.call('pause>nul', shell=True)
