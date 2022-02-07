import json
from difflib import get_close_matches

my_data = json.load(open("Json.json"))
word = input("enter the word: ")
def fun_check(a):
    a = a.lower()
    if a in my_data:
        return my_data[a]
    elif len(get_close_matches(a,my_data.keys())) > 0:
        choice = input("Did you mean %s " %get_close_matches(a,my_data.keys())[0])
        if choice == "Y" or "y":
            return my_data[get_close_matches(a,my_data.keys())[0]]
        elif choice == "N" or "n":
            return " The word doesn't exist, please enter the correct word"
    else:
        return " The word doesn't exist, please enter the correct word"

result = (fun_check(word))
if type(result) == list:
    for i in result:
        print(i)
else:
    print(result)











