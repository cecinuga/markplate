def from_path_to_filename(path: str) -> str:
    return path.split('/')[-1].split('.')[0]
