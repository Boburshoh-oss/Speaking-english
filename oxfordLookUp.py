import requests
from pprint import pprint 


def get_definition(word_id):
    url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word_id}'
    r = requests.get(url)
    res = r.json()
    output = {}

    if type(res)!=list:
        return False
        
    definitions = []
    for meaning in range(len(res[0]['meanings'])):
        for i in range(len(res[0]['meanings'][meaning]['definitions'])):
            definitions.append(f"for {res[0]['meanings'][meaning]['partOfSpeech']} 👉{res[0]['meanings'][0]['definitions'][i]['definition']}")

    # for i in range(len(res[0]['meanings'][1]['definitions'])):
    #     print("adjective variant")
    #     adjective_definitions.append(f"for adjective 👉{res[0]['meanings'][0]['definitions'][i]['definition']}")
    #     pprint(res[0]['meanings'][0]['definitions'][i]['definition'])
    
    output['definitions'] = "\n".join(definitions)

    if res[0]['phonetics'][0].get('audio'):
        output['audio'] = res[0]['phonetics'][0]['audio']
    return output

if __name__=='__main__':
    from pprint import pprint
    pprint(get_definition("Great Britain"))
    pprint(get_definition("america"))