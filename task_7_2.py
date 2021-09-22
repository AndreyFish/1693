
import yaml
import os

with open('config.yaml') as f:
    content = yaml.safe_load(f)

print(content)

def create_path(values, prefix=""):
    for directory, paths in values.items():
        dir_path = os.path.join(prefix, directory)
        os.makedirs(dir_path, exist_ok=True)
        if isinstance(paths, dict):
            create_path(paths, dir_path)
        else:
            for i in paths:
                if isinstance(i, dict):
                    create_path(i, dir_path)
                elif isinstance(i, str):
                    with open(os.path.join(dir_path, f'{i}'), 'w') as _:
                        pass


