# def nums():
    
#     nums1 = [4,9,5]
#     nums2 = [9,4,9,8,4]
#     return list(set(nums1) & set(nums2))
# print(nums())



state_codes = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District Of Columbia': 'DC',
    'Federated States Of Micronesia': 'FM',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Marshall Islands': 'MH',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands': 'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Palau': 'PW',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}



# def state_code(state_name):
#     if len(state_name) < 3:
#         return  "Validation error: Please put at least 3 characters."
#     if len(state_name) > 50:
#         return "Validation error: Please put maximum 50 characters."
    
#     arr = []
#     state_name = state_name.lower()
#     for i in state_codes:
#         if state_name == i.lower():
#             return state_codes[i]
#         elif state_name.lower() in i.lower():
#             arr.append(i)

#     if len(arr) > 0:
#         return "Maybe you mean: " + ' or '.join(arr)
#     else:
#         return "No data found"

# state_name = "ala"
    
# print(state_code(state_name))



# def stat_code(state_name):
#     if len(state_name) < 2:
#         return "Validation error: Please put at least 3 characters"
#     if len(state_name) > 50:
#         return "Validation error: Maximum chars limit exceeded" 
#     if state_name in state_codes:
#         return state_codes[state_name]
#     arr = []
#     for i in state_codes:
#        if state_name == i.lower():

#             return state_codes[i]
#        elif state_name.lower() in i.lower():
#            arr.append(i)

#     if len(arr) > 0:
#         return "Maybe you Mean: " +  ' or '.join(arr)
#     else:
#         return "No Data Found"
    
    

# state_name = 'ala'
# print(stat_code(state_name))







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





# import json

# data = {"name":"Alice",
#         "Age": 30,
#         "Hobbies":["Reading","Coding","Traveling"]
#         }
# json_String = json.dump(data,indent=4,sort_keys=True)
# print(json_String)




# import requests


# def change_rates(amount,base_currency,target_currency):
#     url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"    
 
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         rates = data['rates']
#         if target_currency in rates:
#             exchange_rates = rates[target_currency]
#             converted_amount = amount * exchange_rates
#             return converted_amount
#         else:
#             print(f"Eror: Target currency {target_currency} not found")
#     else:
#         print(f"Error: Failed to fetch exchange rates. Status code:{response.status_code}")
#         return None


# def main():
#     print("welcome to the Currency Converter")
#     user_amount = (input("Enter the amount to converter: "))

#     if user_amount.isdigit() == False:
#         print('Please write numeric value for the amount')
#         return
    
#     amount = float(user_amount)
#     source_currency = input("Enter the source currency: ").upper()
#     target_currency = input("Enter the source currency: ").upper()


#     converted_amount = change_rates(amount,source_currency,target_currency)
#     if converted_amount is not None:
#         print("\nConverted amount")
#         print(f"{amount},{source_currency} is equivalent to {converted_amount:.2f} {target_currency}")

# if __name__ == "__main__":
#     main()
