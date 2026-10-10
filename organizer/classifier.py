from .scanner import FileInfo
from pathlib import Path
from .rules import load_rules, build_extension_map

def categorize_file(file_info: FileInfo,extension_map: dict) -> str:
    
    if   file_info.extension in extension_map:
        file_category = extension_map[file_info.extension]
    else:
     file_category ="Others"
    return file_category