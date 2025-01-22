import os
from charconf import interprete_to_latin

original_dir = [f for f in os.listdir('original/')]

for file in original_dir:
    file_text: str

    with open('original/' + file, 'r', encoding='utf-8', errors='ignore') as read_file:
        file_text = interprete_to_latin((read_file.read()))

    save_path: str = '../ccscript/' if file.endswith('.ccs') else '../'
    
    with open(save_path + file, 'w', encoding='utf-8', errors='ignore') as written_file:
        written_file.write(file_text)

    print(f'File "{file}" was compiled succesfully to "{save_path}"!')

input('_____Press_any_key_to_exit_____')
