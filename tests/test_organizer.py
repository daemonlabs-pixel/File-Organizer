from organizer.organizer import organize_directory
from pathlib import Path
import unittest
import tempfile

class TestOrganizer(unittest.TestCase):
    def test_organize_file(self):
         with tempfile.TemporaryDirectory() as temp_dir:
              test_dir = Path(temp_dir)
              photo_path = test_dir/ "photo.jpg"
              photo_path.touch()
              song_path = test_dir/"song.mp3"
              song_path.touch()
              code_path = test_dir/"code.py"
              code_path.touch()
              excel_path = test_dir/"excel.xls"
              excel_path.touch()
              organize_directory(test_dir)
              self.assertTrue((test_dir/"Images"/"photo.jpg").exists())
              self.assertTrue((test_dir/"Code"/"code.py").exists())
              self.assertTrue((test_dir/"Music"/ "song.mp3").exists())
              self.assertTrue((test_dir/"Spreadsheets"/"excel.xls").exists())

    def test_organize_duplicate_files(self):
         with tempfile.TemporaryDirectory() as temp_dir:
              test_dir= Path(temp_dir)
              photo_path = test_dir/"photo.jpg"
              photo_path.write_text("First photo")
              organize_directory(test_dir)
              self.assertTrue((test_dir/"Images"/"photo.jpg").exists())
              self.assertEqual((test_dir / "Images" / "photo.jpg").read_text(), "First photo")
              photo2_path = test_dir/"photo.jpg"
              photo2_path.write_text("Second photo")
              organize_directory(test_dir)
              self.assertTrue((test_dir/"Images"/"photo(1).jpg").exists())
              self.assertEqual((test_dir / "Images" / "photo(1).jpg").read_text(), "Second photo")



