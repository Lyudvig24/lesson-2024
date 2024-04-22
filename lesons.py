# def nums():
    
#     nums1 = [4,9,5]
#     nums2 = [9,4,9,8,4]
#     return list(set(nums1) & set(nums2))
# print(nums())


#########################################
# state_codes = {
#     'Alabama': 'AL',
#     'Alaska': 'AK',
#     'American Samoa': 'AS',
#     'Arizona': 'AZ',
#     'Arkansas': 'AR',
#     'California': 'CA',
#     'Colorado': 'CO',
#     'Connecticut': 'CT',
#     'Delaware': 'DE',
#     'District Of Columbia': 'DC',
#     'Federated States Of Micronesia': 'FM',
#     'Florida': 'FL',
#     'Georgia': 'GA',
#     'Guam': 'GU',
#     'Hawaii': 'HI',
#     'Idaho': 'ID',
#     'Illinois': 'IL',
#     'Indiana': 'IN',
#     'Iowa': 'IA',
#     'Kansas': 'KS',
#     'Kentucky': 'KY',
#     'Louisiana': 'LA',
#     'Maine': 'ME',
#     'Marshall Islands': 'MH',
#     'Maryland': 'MD',
#     'Massachusetts': 'MA',
#     'Michigan': 'MI',
#     'Minnesota': 'MN',
#     'Mississippi': 'MS',
#     'Missouri': 'MO',
#     'Montana': 'MT',
#     'Nebraska': 'NE',
#     'Nevada': 'NV',
#     'New Hampshire': 'NH',
#     'New Jersey': 'NJ',
#     'New Mexico': 'NM',
#     'New York': 'NY',
#     'North Carolina': 'NC',
#     'North Dakota': 'ND',
#     'Northern Mariana Islands': 'MP',
#     'Ohio': 'OH',
#     'Oklahoma': 'OK',
#     'Oregon': 'OR',
#     'Palau': 'PW',
#     'Pennsylvania': 'PA',
#     'Puerto Rico': 'PR',
#     'Rhode Island': 'RI',
#     'South Carolina': 'SC',
#     'South Dakota': 'SD',
#     'Tennessee': 'TN',
#     'Texas': 'TX',
#     'Utah': 'UT',
#     'Vermont': 'VT',
#     'Virgin Islands': 'VI',
#     'Virginia': 'VA',
#     'Washington': 'WA',
#     'West Virginia': 'WV',
#     'Wisconsin': 'WI',
#     'Wyoming': 'WY'
# }

# def state_code(state_name):
    # return

# state_name = "new" # input("enter stat name ")
    
# print(state_code(state_name))



###########################################################




# def guess_number(guess):
#     numbers = '2019'
#     cow = 0
#     bull = 0

#     for i in range(len(numbers)):
#         if numbers[i] == guess[i]:
#             cow += 1
#         elif guess[i] in numbers:
#             bull += 1
#         else:
#             continue
#     print(cow,bull)
    
        


      
            
        




# guess  = input("enter number ")

# guess_number(guess)


# answer = []

# def words():
#     wovels = "aeouiy"
#     while True:
#         word = input("Entner  word ")
#         if word == "stop":
#             break
#         count = 0
#         for i in word:
#             if i in wovels:
#                 count += 1
#         if count > 2:
#             answer.append(word)
# words()
# print(answer)


# words = "hello word"
# def words_count():
#     mydict = {}
#     for k,v in words.items():
#         if v in mydict:
#             mydict[v].append(k)

#         else:
#             mydict[v] = [k]
#     return mydict

# print(words_count())






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






def weather_check():
    return 1

print(__name__)





# def sumarr(mlist):
#     if mlist == []:
#         return 0
#     else:
#         return mlist[0] + sumarr(mlist[1:])
    
# print(sumarr(mlist=([1,2,3])))



# def quick_sort(mlist):
#     if len(mlist) < 2:
#         return mlist
    
#     pivot = mlist[0]
#     less = [i for i in mlist[1:] if i <= pivot]
#     great = [i for i in mlist[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(great)

# print(quick_sort([12,1,14,16,12,2,2,2,2]))


# def len_arr(mlist):
#     if mlist == []:
#         return 0
#     else:
#         return 1 + len_arr(mlist[1:])
    
# print(len_arr(mlist=([1,2,3])))









