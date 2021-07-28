

# app / robo_advisor.py

import requests
import json #> string to dict

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

# INFO INPUTS

requests_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo"
response = requests.get(requests_url)

parsed_response = json.loads(response.text) #this gets us data in dictionary form

last_refreshed = parsed_response["Meta Data"] ["3. Last Refreshed"]


#breakpoint()

tsd = parsed_response["Time Series (Daily)"]

dates = list(tsd.keys())

latest_day = dates[0]

latest_close = tsd[latest_day]["4. close"]

high_prices = []
low_prices = []

for date in dates:
    high_price = tsd[latest_day]["2. high"]
    high_prices.append(float(high_price))
    low_price = tsd[latest_day]["3. low"]
    low_prices.append(float(low_price))

recent_high = max(high_prices)
recent_low = min(low_prices)

#high_prices = [10,20,30,4]
#recent_high = max(high_prices)


#url =
#r = requests.get(url)
#data = r.json()

#print(data)


# INFO OUTPUTS


#Setup
print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
