# File Counter Python

A Python command-line tool to count lines, words, and characters in files.

## Features

- Count lines, words, and characters in files
- Support for multiple files
- Recursive directory counting
- File type filtering
- Multiple output formats (text, JSON, CSV)

## Installation

```bash
pip install file-counter-python
```

Or clone and install:

```bash
git clone https://github.com/mizoz/file-counter-python.git
cd file-counter-python
pip install -e .
```

## Usage

```bash
# Count all files in directory
file-counter .

# Count specific file
file-counter myfile.txt

# Count with details
file-counter --verbose myfile.txt

# Recursive counting
file-counter --recursive ./src

# JSON output
file-counter --format json .
```

## Options

- `-r, --recursive` - Recursively count files in subdirectories
- `-v, --verbose` - Show detailed output
- `-t, --types` - Specify file types to count
- `-f, --format` - Output format (text, json, csv)

## Python API

```python
from file_counter import FileCounter

counter = FileCounter()
result = counter.count('example.txt')
print(f"Lines: {result['lines']}")
print(f"Words: {result['words']}")
print(f"Characters: {result['characters']}")
```

## License

MIT License

## Author

mizoz
