from .classifier import categorize_file
from .scanner import scan_directory
from .rules import prepare_extension_map
from pathlib import Path
from .file_utils import get_unique_path

def organize_directory(path : Path):
    files = scan_directory(path)
    extension_map = prepare_extension_map()
    for file_info in files:
        categorized_file =categorize_file(file_info, extension_map)
        category_folder = path/ categorized_file
        category_folder.mkdir(exist_ok=True)
        destination = category_folder/ file_info.name
        destination =get_unique_path(destination)
        file_info.path.rename(destination)
    
       
