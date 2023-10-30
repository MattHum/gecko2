#import requests
#import json
#import csv

from creds import apikey
ak = apikey
print(ak)

newstring = "&vs_currencies=" + "eur" + "&include_market_cap=" + "false" + "&include_24hr_vol=" + "false" + "&include_24hr_change=" + "false" + "&include_last_updated_at=" + "false" + "&precision=" + "false" + "&x_cg_demo_api_key=" + ak
print(newstring)