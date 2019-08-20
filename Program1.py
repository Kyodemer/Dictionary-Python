import json
from difflib import get_close_matches

data = json.load(open("dictonary1"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter yes if yes, or no if no. " % get_close_matches(word, data.keys())[1])
        if yn == "yes":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "no":
            return "The word doesn't exists. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exists. Please double check it. "


word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
