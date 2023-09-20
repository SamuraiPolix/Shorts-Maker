import json


def get_data(json_file):
    with open(f'{json_file}', 'r', encoding='utf-8') as f:
        jsonData = json.load(f)
    verses: str = jsonData['verses']
    refs: str = jsonData['references']
    return verses, refs


def fix_json_structure(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    verses = data['verses']
    references = data['references']

    fixed_data = {'verses': []}

    for i in range(len(verses)):
        verse = verses[i]
        reference = references[i]
        fixed_data['verses'].append({'verse': verse, 'reference': reference})

    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(fixed_data, file, indent=4, ensure_ascii=False)


def restore_json_structure(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    verses = []
    references = []

    for verse_data in data['verses']:
        verse = verse_data['verse']
        reference = verse_data['reference']
        verses.append(verse)
        references.append(reference)

    restored_data = {
        'verses': verses,
        'references': references
    }

    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(restored_data, file, indent=4, ensure_ascii=False)