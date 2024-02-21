import sys
import requests
import json

if len(sys.argv) == 2:
    try:
        n = float(sys.argv[1])
    except:
        sys.exit(1)
else:
    sys.exit(1)


try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    pass
response = response.json()
result = round(n * response["bpi"]["USD"]["rate_float"], 4)
print(f"${result:,}")
