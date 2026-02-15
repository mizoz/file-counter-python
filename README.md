# File Counter Python

[![PyPI Version](https://img.shields.io/pypi/v/file-counter-python?style=flat-square)](https://pypi.org/project/file-counter-python/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/file-counter-python?style=flat-square)](https://pypi.org/project/file-counter-python/)
[![License](https://img.shields.io/pypi/l/file-counter-python?style=flat-square)](LICENSE)
[![Python Version](https://img.shields.io/pypi/pyversions/file-counter-python?style=flat-square)](https://pypi.org/project/file-counter-python/)
[![GitHub Stars](https://img.shields.io/github/stars/mizoz/file-counter-python?style=flat-square)](https://github.com/mizoz/file-counter-python)

> A Python CLI tool for counting lines, words, and characters in files.

## Features

- Count lines in files
- Count words in files
- Count characters in files
- Recursive directory counting
- Multiple file support
- Python API for integration

## Installation

### From PyPI

```bash
pip install file-counter-python
```

### From Source

```bash
git clone https://github.com/mizoz/file-counter-python.git
cd file-counter-python
pip install -e .
```

## Usage

### Command Line

```bash
# Count a single file
file-counter myfile.txt

# Count multiple files
file-counter file1.txt file2.txt

# Count all files in directory
file-counter --recursive myfolder/

# Detailed output
file-counter --verbose myfile.txt
```

### Python API

```python
from file_counter import FileCounter

counter = FileCounter()

# Count a file
result = counter.count("myfile.txt")
print(result)  # {lines: 100, words: 500, chars: 3000}
```

## CLI Options

| Option | Description |
|--------|-------------|
| `-r, --recursive` | Recursively count files |
| `-v, --verbose` | Detailed output |

## Requirements

- Python 3.7+

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Author

**mizoz**
- GitHub: [@mizoz](https://github.com/mizoz)

---

⭐ If you find this project useful, please consider giving it a star on GitHub!
