import json
import requests
import sys
try:
    if len(sys.argv)!=2:
        sys.exit("Missing command-line argument")
    sys.argv[1]=float(sys.argv[1])
    n=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    #print(json.dumps(n.json(),indent=2))
    obj=n.json()
    amount = obj["bpi"]["USD"]["rate_float"] * float(sys.argv[1])

    print(f"${amount:,.4f}")


except requests.RequestException:
    print("Requests Failed")
except ValueError:
    sys.exit("Command-line argument is not a number")



