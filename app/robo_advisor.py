

# app / robo_advisor.py

import requests
import json #> string to dict

# INFO INPUTS

requests_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo"
response = requests.get(requests_url)
#print(type(response))
#print(response.status_code)
#print(response.text) #know this is a string

parsed_response = json.loads(response.text) #this gets us data in dictionary form

last_refreshed = parsed_response["Meta Data"] ["3. Last Refreshed"]
#breakpoint()


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
print("LATEST CLOSE: $100,000.00")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
