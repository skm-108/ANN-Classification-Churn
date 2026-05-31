import json
nb=json.load(open('experiments.ipynb',encoding='utf-8'))
print('metadata:', json.dumps(nb.get('metadata',{}), indent=2))
