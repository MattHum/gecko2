#getting data from coingecko via API-Demo, datasourec: coingecko, Okt 2023
import requests
import json
import csv

#build api request

#from FAQ/coingecko
#response = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin&x_cg_demo_api_key=API")
#response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=eur&include_market_cap=false&include_24hr_vol=false&include_24hr_change=false&include_last_updated_at=false&precision=false&x_cg_demo_api_key=API")
#response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=eur&include_market_cap=false&include_24hr_vol=false&include_24hr_change=false&include_last_updated_at=false&precision=false&x_cg_demo_api_key=API")
#response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=(payload)&vs_currencies=eur&include_market_cap=false&include_24hr_vol=false&include_24hr_change=false&include_last_updated_at=false&precision=false&x_cg_demo_api_key=API")

url = "https://api.coingecko.com/api/v3/simple/price?ids="
from creds import apikey
ak = apikey
my_list = ['bitcoin', 'bitcoin-cash', 'zcash', 'ethereum', 'litecoin', 'monero', 'dash', 'cardano', 'ripple', 'neo', 'eos', 'stellar', 'crypterium', 'polkadot', 'solana', 'dydx', 'matic-network', 'algorand', 'cosmos']
#polygon => matic-network
separator =','
payload = separator.join(my_list)
newstring = url + payload + "&vs_currencies=" + "eur" + "&include_market_cap=" + "false" + "&include_24hr_vol=" + "false" + "&include_24hr_change=" + "false" + "&include_last_updated_at=" + "false" + "&precision=" + "false" + "&x_cg_demo_api_key=" + ak
response = requests.get(newstring) #call api
API_data = response.json() #save json replay in dict
print(response.status_code) # check if connection went ok = 200

#save data from nested dict to regular dict
API_data_cleen = {}
for i, j in API_data.items():
  API_data_cleen[i] = API_data[i]['eur']

#re-order dict -> according to the my_list order
API_data_cleen_order = {}
for item in my_list:
  API_data_cleen_order[item] = API_data_cleen[item]

#convert float to string and change point/comma
for i, j in API_data_cleen_order.items():
  test = f'{API_data_cleen_order[i]:.2f}' #convert float/int to string 
  API_data_cleen_order[i] = test.replace('.', ',') #replace point with comma
  
#print(API_data_cleen_order)
for i, j in API_data_cleen_order.items():
  print(i,';',j)  

# Export: create csv, Open the file in writing mode (no blank lines)  
with open('coin_prices.csv', 'w') as f: #path -> C:\Users\HP
    for key, value in API_data_cleen_order.items():
        f.write(f'{key};{value}\n')