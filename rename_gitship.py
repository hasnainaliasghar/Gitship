import os

def replace_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content.replace('Gitship', 'Gitship')
        new_content = new_content.replace('gitship', 'gitship')
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filepath}")
    except Exception as e:
        print(f"Error reading {filepath}: {e}")

for root, dirs, files in os.walk('.'):
    if '.git' in root or '__pycache__' in root or 'repos' in root or 'static' in root or 'venv' in root:
        continue
    for file in files:
        if file.endswith(('.py', '.jinja', '.md', '.txt')):
            replace_in_file(os.path.join(root, file))
