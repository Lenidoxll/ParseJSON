import json

fname = 'root.json'

with open(fname, 'r') as f:
    with open(f'{fname}_parsing.txt', 'w') as newf:
        data = json.load(f)
        field_name, field_value = 'blockName', 'blockValues'
        for obj in data['state']['objects'].values():
            if field_name in obj and field_value in obj:
                newf.write(f'<h2>Параметры {obj[field_name]}:</h2>\n<ul>\n')
                for val in obj[field_value]:
                    newf.write(f'\t<li>{val} = {obj[field_value][val]}</li>\n')
                newf.write(f'</ul>\n')