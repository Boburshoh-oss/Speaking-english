import requests
from pprint import pprint 
import json
from JsonExtract import jsonExtract

app_id = "62b446b5"
app_key = "c2fe6960887f53b88999a767283d7e34"

endpoint = "entries"
language_code = "en-us"
word_id = "cover"

url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word_id}'
# url = "https://od-api.oxforddictionaries.com/api/v2/" + endpoint + "/" + language_code + "/" + word_id.lower()
# API_KEY = "d80877eba15d2ee262b3a489"
# currency = 'USD'
# url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"
r = requests.get(url)
res = r.json()
print(res)
for i in range(len(res[0]['meanings'][0]['definitions'])):
    print("noun variant")
    pprint(res[0]['meanings'][0]['definitions'][i]['definition'])
    

for i in range(len(res[0]['meanings'][1]['definitions'])):
    print("adjective variant")
    pprint(res[0]['meanings'][0]['definitions'][i]['definition'])
# print(res)
# print(res[0]['meanings'][0]['definitions'][0]['definition'])
# print(res[0]['meanings'][0]['definitions'][1]['definition'])
# print(res[0]['meanings'][0]['definitions'][2]['definition'])
print(res[0]['phonetics'][0]['audio'])

# print("code {}\n".format(r.status_code))
# pprint(r.json())
# print("text \n" + r.text)
# print("json \n" + json.dumps(r.json()))

