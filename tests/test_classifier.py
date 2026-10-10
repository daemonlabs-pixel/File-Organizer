from organizer.scanner import FileInfo
from organizer.rules import prepare_extension_map
from organizer.classifier import categorize_file
from pathlib import Path
import unittest
import tempfile


class TestClassifier(unittest.TestCase):
    def test_categorize_file(self):
        extension_map = prepare_extension_map()
        file_jpg = FileInfo( path = Path("file.jpg"),  name ="file_jpg", extension =".jpg", size = 100)
        unknown_file = FileInfo(path =Path("file.unknown"), name ="file_unknown", extension =".xyz", size =100)
        file_mp3 = FileInfo(path = Path("file.mp3"), name ="file_mp3", extension =".mp3", size = 200)
        self.assertEqual(categorize_file(file_jpg,extension_map), "Images")
        self.assertEqual(categorize_file(unknown_file, extension_map), "Others")
        self.assertEqual(categorize_file(file_mp3, extension_map), "Music")

    