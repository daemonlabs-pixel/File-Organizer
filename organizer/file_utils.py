from importlib.resources import path
from pathlib import Path
def check_hidden(path: Path) -> bool:
    file_name = path.name
    if file_name.startswith("."):
        return True
    return False

def get_extension(path:Path) -> str:
    file_suffix = path.suffix.lower()
    return file_suffix
    
def get_unique_path(path:Path) -> Path:
   if not path.exists():
       return path
   count= 1
   new_file_name =path.stem + f"({count})" + path.suffix
   new_path =path.with_name(new_file_name)
   while new_path.exists():
        count+= 1
        new_file_name =path.stem + f"({count})" + path.suffix
        new_path =path.with_name(new_file_name)
   return new_path