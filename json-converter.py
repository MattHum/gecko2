import requests
#import json
#import csv

url = "https://api.coingecko.com/api/v3/simple/price?ids="
from creds import apikey
ak = apikey

dict_http = {'vs_currencies=':'eur', 'include_market_cap=':'false', 'include_24hr_vol=':'false', 'include_24hr_change=':'false', 'include_last_updated_at=':'false', 'precision=':'false', 'x_cg_demo_api_key=':ak}
#req = requests.Request('GET', url , params=dict_http)
r = requests.get(url, params=dict_http)
#prepared = req.prepare() # Get a PreparedRequest object
print (r.url)

my_list = ['bitcoin', 'bitcoin-cash', 'zcash', 'ethereum', 'litecoin', 'monero', 'dash', 'cardano', 'ripple', 'neo', 'eos', 'stellar', 'crypterium', 'polkadot', 'solana', 'dydx', 'matic-network', 'algorand', 'cosmos']
#polygon => matic-network