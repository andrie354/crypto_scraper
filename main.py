import requests
import time
import pandas as pd


url = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing"

res = []

for x in range(1,72):
    querystring = {"start":f"{x}","limit":"100","sortBy":"market_cap","sortType":"desc","convert":"USD,BTC,ETH","cryptoType":"all","tagType":"all","audited":"false","aux":"ath,atl,high24h,low24h,num_market_pairs,cmc_rank,date_added,max_supply,circulating_supply,total_supply,volume_7d,volume_30d"}

    headers = {
        "authority": "api.coinmarketcap.com",
        "pragma": "no-cache",
        "cache-control": "no-cache",
        "sec-ch-ua": "^\^Google"
    }

    r = requests.request("GET", url, headers=headers, params=querystring)

    time.sleep(2)

    data = r.json()

    for p in data['data']['cryptoCurrencyList']:
        res.append(p)
        print('crypto found: ', len(res))


df = pd.json_normalize(res)
print(df.head(), df.tail())
df.to_csv('crypto.csv')
