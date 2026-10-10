# File Organizer

A Python application that organizes files in a directory into category-based folders according to their file extensions.

## Features

- Scans files directly inside a selected directory.
- Skips hidden files.
- Categorizes files according to their extensions.
- Creates category folders automatically.
- Moves files into their corresponding category folders.
- Prevents overwriting files by generating unique filenames when duplicates exist.
- Handles invalid directory paths.
- Includes automated unit tests using Python's built-in `unittest` framework.

**Note:** The organizer processes files directly inside the selected directory. It does not recursively scan subdirectories.

## Requirements

- Python 3.11 or later.
- No external Python packages are currently required.

## Project Structure

```text
File organizer/
├── app.py
├── organizer/
│   ├── __init__.py
│   ├── file_utils.py
│   ├── rules.py
│   ├── scanner.py
│   ├── classifier.py
│   └── organizer.py
├── ui/
│   ├── __init__.py
│   └── cli.py
├── tests/
│   ├── __init__.py
│   ├── test_file_utils.py
│   ├── test_scanner.py
│   ├── test_classifier.py
│   └── test_organizer.py
├── config/
│   └── rules.json
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Use

1. Open a terminal in the project root directory.
2. Run the application:

   ```bash
   python app.py
   ```

3. Enter the path to the directory you want to organize when prompted.

   Example on Windows:

   ```text
   E:\MyFiles
   ```

4. The application creates category folders and moves matching files into them.

**Important:** The organizer moves files rather than copying them. Test it on a directory containing sample files before using it on important data.

## Duplicate Files

If a destination filename already exists, the organizer generates a unique filename rather than overwriting the existing file.

For example:

```text
photo.jpg
photo(1).jpg
photo(2).jpg
```

## Running the Tests

The project uses Python's built-in `unittest` framework. No additional testing package is needed.

Run all tests from the project root:

```bash
python -m unittest discover -s tests -v
```

To run an individual test module:

```bash
python -m unittest tests.test_file_utils -v
python -m unittest tests.test_scanner -v
python -m unittest tests.test_classifier -v
python -m unittest tests.test_organizer -v
```

### Test Coverage

| Test module | What it checks |
|---|---|
| `test_file_utils.py` | Hidden-file detection, extension normalization, and unique filenames |
| `test_scanner.py` | File scanning, hidden-file exclusion, directory filtering, and invalid paths |
| `test_classifier.py` | Correct categories and fallback to `Others` |
| `test_organizer.py` | File organization and duplicate filename handling |

The current test suite contains **9 tests**, all of which passed in the latest test run.

## Error Handling

The command-line interface handles invalid directory paths and operating-system errors by displaying an error message.

## Dependencies

The project currently uses only Python's standard library. The `requirements.txt` file can remain empty until external dependencies are introduced.