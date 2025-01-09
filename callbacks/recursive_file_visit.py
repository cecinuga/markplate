import os
from os import listdir

input_dir = execution_callback_dir # type: ignore
exclude_item = exclude #type: ignore

def from_path_to_filename(path: str) -> str:
    return path.split('/')[-1]

def from_path_to_repopath(path: str) -> str:
    return '/'.join(path.split('/')[-3:]) #TODO: make path depth dynamic

def recursive_visit(path: str, output: list[str]=[]) -> list[str]:
    if os.path.isfile(path): 
        output.append(path)
    else:
        for item in listdir(path):
            if item not in exclude_item:
                recursive_visit(f'{path}/{item}')
    
    return output

if __name__ == '__main__':
    file_list = recursive_visit(input_dir)
    result = [ {  
                'name': from_path_to_filename(file).replace('_', '-'), 
                'path': from_path_to_repopath(file),
                'difficulty': from_path_to_repopath(file).split('/')[0],
                'language': from_path_to_repopath(file).split('/')[1]
            } for file in file_list ] 