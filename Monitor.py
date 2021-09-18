import urllib3, json, os, time, random, threading
webhook = "https://discord.com/api/webhooks/869744468918669323/DmPdiOonixH0ZbpEmadtcoB_OhGFafbylR5_bVnX8glvtDaKYx1mvxKU6pC5kgPRTLJ9"
api1 = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
api2 = "https://api.binance.com/api/v3/trades"  # Different Api For Possible Answers
api1_headers = {
    "X-CMC_PRO_API_KEY": "54d65d34-156b-4906-8224-274fef123e74",
    "Accept": "application/json",
}

while True:
    req = urllib3.PoolManager()
    res = req.request("GET", api1, headers=api1_headers)
    js = json.loads(res.data)
    symbol1 = js["data"][0]["symbol"]
    symbol2 = js["data"][1]["symbol"]
    price1 = js["data"][0]["quote"]["USD"]["price"]
    price2 = js["data"][1]["quote"]["USD"]["price"]
    # market_cap = js['data'][0]['quote']['market_cap']
    change1 = js["data"][0]["quote"]["USD"]["percent_change_1h"]
    change2 = js["data"][1]["quote"]["USD"]["percent_change_1h"]
    supply1 = js['data'][0]['total_supply']
    supply2 = js['data'][1]['total_supply']
    embed1 = {
        "username": "Bitcoin Price Monitor",
        "avatar_url": "https://s2.coinmarketcap.com/static/img/coins/200x200/1.png",
        "embeds": [
            {
                "author": {
                    "name": "Windex",
                    "url": "https://bit.ly/39k2B20",
                    "icon_url": "https://nulled.gay/V1x48R.png",
                },
                "title": "Bitcoin Price",
                "url": "https://coinmarketcap.com/currencies/bitcoin/",
                "description":"Gets The Price of BTC every 15 Seconds.",
                "color": 15069440,
                "fields": [
                    {
                        "name": "`Bitcoin Price`",
                        "value": f"**Current Price**: {price1}\nPrice Change(in last hour): {change1}\n**Total Supply**:{supply1}",
                        "inline": False,
                    }
                ],
                "footer": {
                    "text": f"Request Made: {time.ctime(time.time())}.\n\nPrices Are USD."
                },
            }
        ],
    }
    embed2 = {
        "username": "Ethereum Price Monitor",
        "avatar_url": "https://avatars.githubusercontent.com/u/6250754?s=200&v=4",
        "embeds": [
            {
                "author": {
                    "name": "Windex",
                    "url": "https://bit.ly/39k2B20",
                    "icon_url": "https://nulled.gay/V1x48R.png",
                },
                "title": "Ethereum Price",
                "url": "https://coinmarketcap.com/currencies/ethereum/",
                "description":"Gets The Price of ETH every 15 Seconds.",
                "color": 0,
                "fields": [
                    {
                        "name": "`Ethereum Price`",
                        "value": f"**Current Price**: {price2}\n**Price Change(in last hour)**: {change1}\n**Total Supply**:{supply2}",
                        "inline": False,
                    }
                ],
                "footer": {
                    "text": f"Request Made: {time.ctime(time.time())}.\n\nPrices Are USD."
                },
            }
        ],
    }
    req.request(
        "POST",
        webhook,
        body=json.dumps(embed1),
        headers={"Content-Type": "application/json"},
    )
    req.request(
        "POST",
        webhook,
        body=json.dumps(embed2),
        headers={"Content-Type": "application/json"},
    )
    time.sleep(15)