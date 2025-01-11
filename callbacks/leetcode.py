from callbacks.lib.path_utils import from_path_to_filename
from callbacks.lib.recursive_file_visit import recursive_visit

input_dir = execution_callback_dir # type: ignore
exclude_item = exclude #type: ignore

def from_path_to_repopath(path: str) -> str:
    return '/'.join(path.split('/')[-3:]) #TODO: make path depth dynamic

if __name__ == '__main__':
    file_list = recursive_visit(input_dir, exclude_item)
    result = [
        [ {  
                'name': from_path_to_filename(file).replace('_', '-'), 
                'path': from_path_to_repopath(file),
                'difficulty': from_path_to_repopath(file).split('/')[0],
                'language': from_path_to_repopath(file).split('/')[1]
            } for file in file_list ],
        'cecinuga'
        ]