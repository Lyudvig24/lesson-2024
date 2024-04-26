# #Program crypto stats
# import requests
# import time
# import json



# def crypto_stats(name_filter,name_value):
    

     
#         url = 'https://api.coingecko.com/api/v3/coins/markets'
#         params = {
#             'vs_currency': 'usd',
#             'order': 'market_cap_desc',
#             'per_page': '20',
#             'page': '1',
#             'sparkline': 'false',
#             'price_change_percentage': '24h',
#             'market_data': 'true'
#         }
#         try:
        
#             while True:
#                     response = requests.get(url, params=params)
#                     data = response.json()
#                     symbol = ""
#                     for i in data:
                        
#                         name = i['name']
#                         symbol = i['symbol'].upper()
#                         current_price = i['current_price']
#                         market_cap = i['market_cap']
#                         price_change_24 = i['price_change_percentage_24h']

#                         if name_filter and name_filter.lower() and name_filter != symbol.lower():
#                             continue
#                         if name_value and market_cap < name_value:
#                             continue

#                         print(f"Name: {name}, Symbol: {symbol}, Current_Price: {current_price}, Market_cap: {market_cap}, 24h Change: {price_change_24}")
                    
#                     print("----------------")
#                     time.sleep(5)

#         except Exception as e:
#             print("Please Wait:", e)

# if __name__ == "__main__":
#     name_filter = input("Write Cryto name: ")
#     name_value = input("Write  value: ")
    
#     if name_value:
        

#         name_value = float(name_value)
        
        
#         name_value = None

#     print("Crypto price for the last 24 hours")
#     crypto_stats(name_filter,name_value)