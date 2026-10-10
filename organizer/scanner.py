from pathlib import Path
from dataclasses import dataclass
from .file_utils import check_hidden, get_extension

@dataclass
class FileInfo:
    path: Path
    name: str
    extension: str
    size: int

def scan_directory( directory: Path) -> list[FileInfo]:
    file_info_list =[]
    if not directory.is_dir():
        raise ValueError(f"{directory} is not a valid directory.")
    for file_path in directory.iterdir():
        if file_path.is_file():
            if not check_hidden(file_path):
                file_info = FileInfo(
                    path =file_path,
                    name =file_path.name,
                    extension = get_extension(file_path),
                    size = file_path.stat().st_size
                )
                file_info_list.append(file_info)
    return sorted(file_info_list, key = lambda file: file.name) # here it sorts in alphabetical order by name 