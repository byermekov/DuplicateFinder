# Duplicate Image Finder

Duplicate Image Finder is a Python script that helps locate duplicate image files by using CRC32 hash. It calculates the CRC32 hash for each image file and identifies duplicates based on the hash values. This can be useful for cleaning up your image collection or identifying redundant files.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/DuplicateFinder.git
   ```
2. Change into the project directory:
   ```
   cd DuplicateFinder
   ``` 

## Usage

- run python.py with following arguments:
```
python duplicate.py --folders /path/to/folder1 /path/to/folder2 --hash_size 5
```
(Note: folders - supports searching indefinite number of paths, hash_size is set to 5 by default)
