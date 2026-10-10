from pathlib import Path
from organizer.organizer import organize_directory
def main():
    directory = Path(input("Enter the directory path: "))
    try:
        organize_directory(directory)
        print("Files have been organized successfully.")
    except ValueError as error:
        print(f" Error: {error}")
    except OSError as error:
        print(f" OS Error: {error}")