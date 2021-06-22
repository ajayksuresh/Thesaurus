import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def instance(word):
    if word in data:
        return(data[word])
    elif word.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]
    elif len(get_close_matches(word,data.keys())) > 0:
        yn = input(f'Did you mean {get_close_matches(word,data.keys())[0]} instead? Enter y for yes and n for no: ')
        if yn == "y":
            return data[get_close_matches(word,data.keys())[0]]  
        elif yn =='n':
            return("Word not found, enter a diff word")
        else:
            return "Invalid key pressed"
    else:
        return("Word not found, enter a diff word")

w = input("Enter the word you want to search ").lower()
print(instance(w))