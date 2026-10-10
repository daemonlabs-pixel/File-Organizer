import unittest
import tempfile
from pathlib import Path
from organizer.file_utils import check_hidden, get_extension, get_unique_path


class TestFileUtils(unittest.TestCase):
    def test_check_hidden(self):
        hidden_path = Path(".hidden_file.txt")
        visible_path = Path("visible.txt")
        self.assertTrue(check_hidden(hidden_path))
        self.assertFalse(check_hidden(visible_path))

    def test_get_extension(self):
        file_path = Path("example.txt")
        file_path_1 = Path("example.JPG")
        self.assertEqual(get_extension(file_path), ".txt")
        self.assertEqual(get_extension(file_path_1), ".jpg")

    def test_get_unique_path(self):
        with tempfile.TemporaryDirectory() as test_dir:
            test_path = Path(test_dir)/ "test_file.txt"
            unique_path = get_unique_path(test_path)
            self.assertEqual(test_path,unique_path) # Should return the same path, since the file doesn't exist yet
            test_path.touch()  # Create the file
            unique_path = get_unique_path(test_path)# here unique_path should be different because the file already exists, with a (1) append in the name of the file in the path
            self.assertEqual(unique_path, test_path.with_name("test_file(1).txt")) # should return the same path  with  (1) appended to the name