from organizer.scanner import scan_directory
from pathlib import Path
import unittest
import tempfile

class TestScanner(unittest.TestCase):
    # given a valid folder path it created a list containning informations about the files, here it's only files which are not hidden and aren't inside another folder
    def test_scan_directory(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            test_dir = Path(temp_dir)
            photo_path= test_dir/ "photo.jpg" # create a Path object for the file photo.jpg in the temporary directory
            photo_path. touch() # create an empty file named photo.jpg in the temporary directory
            document_path = test_dir/"document.pdf"
            document_path. touch()
            scanned_files = scan_directory(test_dir) 
            self.assertEqual(len(scanned_files),2) # check whether scanned_files contains 2 files
            self.assertEqual(scanned_files[0].name, "document.pdf") # here document.pdf comes first because it is sorted in alphabetical order by name
            self.assertEqual(scanned_files[1].name, "photo.jpg") # here photo.jpg comes second because it is sorted in alphabetical order by name
   
    
    # check the folder and skip the hidden files and the folder inside the parent folder
    def test_scan_directory_with_hidden_files(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            test_dir =Path(temp_dir)
            hidden_file_path =test_dir/".hidden.file.txt"
            hidden_file_path.touch()
            visible_path = test_dir/ "visible.txt"
            visible_path.touch()
            subdirectory_path = test_dir/ "subdirectory"
            subdirectory_path.mkdir()
            scanned_files = scan_directory(test_dir)
            self.assertEqual(len(scanned_files), 1) # check whether scanned_files contain 1 fileInfo why one because scan_directory skips the hidden files
            self.assertEqual(scanned_files[0].name, "visible.txt")
    
    
    # check if the given path is a valid path, a folder path
    def test_scan_directory_invalid_path(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            test_dir = Path(temp_dir)
            file_path = test_dir/ "test.txt"
            file_path.touch()
            with self.assertRaises(ValueError):
                scan_directory(file_path)