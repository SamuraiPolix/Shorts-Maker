import json


def get_data(json_file):
    with open(f'{json_file}', 'r', encoding='utf-8') as f:
        jsonData = json.load(f)
    verses: str = jsonData['verses']
    refs: str = jsonData['references']
    return verses, refs