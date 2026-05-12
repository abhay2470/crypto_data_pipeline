import requests
import pandas as pd
from datetime import datetime
import os
import logging

#API endpoint for fetching cryptocurrency data
API_URL = "https://api.coingecko.com/api/v3/simple/price"

#query parameters for the API request
PARAMS = {
    'ids': 'bitcoin,ethereum,ripple,litecoin,cardano',  # List of cryptocurrencies to fetch
    'vs_currencies': 'usd',
    'last_updated_at': 'True'}

# Make the API request
response = requests.get(API_URL, params=PARAMS)

# Error Handling
if response.status_code != 200:
    print("API Request Failed")
    print("Status Code:", response.status_code)
    exit()

# convert response to JSON format
data=response.json()

#  Create structured records
records=[]

for coin,details in data.items():
    records.append({
        "coin": coin,
        "price_usd": details['usd'],
        "last_updated": details.get('last_updated_at', 'N/A'),
        "ingestion_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
        })
    
# convert to DataFrame
df = pd.DataFrame(records)    

# create output Directory
output_folder = "output"

os.makedirs(output_folder, exist_ok=True)

# generate filename with timestamp
filename = os.path.join(
    output_folder,
    f"crypto_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
)


# save to CSV
df.to_csv(filename, index=False)

print("data ingestion successfully")
print(df)
print(f"\nSaved File Location: {filename}")
