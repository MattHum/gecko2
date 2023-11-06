import requests
#import json
#import csv

from creds import apikey
ak = apikey

url = "https://api.coingecko.com/api/v3/simple/price?ids="
my_list = ['bitcoin', 'bitcoin-cash', 'zcash', 'ethereum', 'litecoin', 'monero', 'dash', 'cardano', 'ripple', 'neo', 'eos', 'stellar', 'crypterium', 'polkadot', 'solana', 'dydx', 'matic-network', 'algorand', 'cosmos']
#polygon => matic-network
separator =','
payload = separator.join(my_list)
newurl = url + payload

dict_http = {'vs_currencies':'eur','include_market_cap':'false', 'include_24hr_vol':'false', 'include_24hr_change':'false', 'include_last_updated_at':'false', 'precision':'false', 'x_cg_demo_api_key':ak}
#req = requests.Request('GET', url , params=dict_http)
r = requests.get(newurl, params=dict_http)
#prepared = req.prepare() # Get a PreparedRequest object
#print (r.url)
API_data = r.json() 
#save json replay in dict
print(r.status_code)

