import json
from difflib import get_close_matches
data = json.load(open("data.json"))
def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("did you mean %s instead : " %get_close_matches(word, data.keys())[0])
        decide = input("if yes than press y or no than n : ")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "n":
            return("plz enter the correct word and try again ")
        else:
            return("you have entered wrong word plz enter y or n")
    else:
        print("plz try another word")
word = input("entar a meaningfull word :  ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
