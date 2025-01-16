import os
from os import listdir

def recursive_visit(path: str, exclude_item:str, output: list[str]=[]) -> list[str]:
    if os.path.isfile(path): 
        output.append(path)
    else:
        list_dir = listdir(path)
        list_dir.reverse()
        for item in list_dir:
            if item not in exclude_item:
                recursive_visit(f'{path}/{item}', exclude_item)
    
    return output