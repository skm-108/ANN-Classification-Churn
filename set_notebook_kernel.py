import json
from pathlib import Path
nb_path = Path('experiments.ipynb')
nb = json.loads(nb_path.read_text(encoding='utf-8'))
nb.setdefault('metadata', {})
nb['metadata']['kernelspec'] = {
    'name': 'annclassification-venv',
    'display_name': 'annclassification (.venv)',
    'language': 'python'
}
nb_path.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding='utf-8')
print('kernelspec set to annclassification-venv')
