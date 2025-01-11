from callbacks.lib.path_utils import from_path_to_filename
from callbacks.lib.recursive_file_visit import recursive_visit

input_dir = execution_callback_dir # type: ignore
exclude_item = exclude #type: ignore

def get_complexity(algo):
    match algo:
        case 'linear_search':
            return 'n'
        case 'binary_search':
            return 'log n'
        case 'insertion_sort':
            return 'n^2'
        case 'merge_sort':
            return 'nlog n'
        

def capital_name(name: str) -> str:
    return ' '.join([ f'{name[0].capitalize()}{name[1:]}' for name in name.split('_')])

if __name__ == '__main__':
    file_list = recursive_visit(input_dir, exclude_item)
    category: str = input_dir.split('/')[1]


    algorithms = [ {  
                'name': capital_name(from_path_to_filename(file)), 
                'complexity': get_complexity(from_path_to_filename(file)),
        } for file in file_list ]
    algorithms.reverse()
    result = [
        algorithms,
        f'./source/{category.lower()}_complexity.png',
        f'{category} Algorithm Complexity Analisys ( worst case )'
    ]

    
