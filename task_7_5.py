import os
import json
import django


def dir_info():
    root_dir = django.__path__[0]
    django_fales = {}
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            size = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))
            ext = file.rsplit('.', maxsplit=1)[-1].lower()
            if size in django_files:
                django_files[size][0] += 1
                if ext not in django_files[size][1]:
                    django_files[size][1].append(ext)
            else:
                django_files[size] = [1, [ext]]

    result = {}
    for size, list_log in sorted(django_files.items()):
        result[size] = tuple(list_log)
        print(f'{size}: {tuple(list_log)}')

    folder_name = os.path.basename(os.getcwd()) + '_sammary.json'
    with open(folder_name, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)


