```markdown
# Secure Password Generator 🔐

A command-line password generator written in Python 3.

This tool generates strong and unpredictable passwords using Python's
cryptographically secure `secrets` module. It also supports custom password
lengths, removing ambiguous characters, disabling special characters, and
copying the generated password to the clipboard.

## Features

- Generates secure random passwords.
- Uses Python's `secrets` module instead of `random`.
- Guarantees at least one lowercase letter, uppercase letter, digit, and
  special character when those character groups are enabled.
- Supports custom password length.
- Can remove ambiguous characters such as `I`, `l`, `1`, `O`, `o`, and `0`.
- Supports generating passwords without special characters.
- Can copy the generated password to the clipboard.
- Provides a command-line interface using `argparse`.
- Validates user input and handles errors.

## Requirements

- Python 3.8 or newer
- `pyperclip`

Install the Python dependency:

```bash
python3 -m pip install pyperclip
```

## Installation

Clone the repository:

```bash
git clone https://github.com/mohammadno09199-bit/password_gen.git
cd password_gen
```

Install the required package:

```bash
python3 -m pip install -r requirements.txt
```

## Usage

Run the program with the default settings:

```bash
python3 password_gen.py
```

Example output:

```text
[+] Generated Password: ExampleGeneratedPassword123!
[+] Length: 24
[*] Password copied to clipboard!
```

## Command-Line Options

Display the help message:

```bash
python3 password_gen.py --help
```

Generate a 32-character password:

```bash
python3 password_gen.py --length 32
```

Generate a password without ambiguous characters:

```bash
python3 password_gen.py --length 24 --ambiguous
```

Generate a password without special characters:

```bash
python3 password_gen.py --length 24 --no-special
```

## Clipboard Support on Linux

If `pyperclip` fails on your system, install a clipboard tool:

For X11: `sudo apt install xclip`
For Wayland: `sudo apt install wl-clipboard`

If clipboard support is unavailable, use the `--no-copy` flag:

```bash
python3 password_gen.py --no-copy
```

## Project Structure

```text
.
├── password_gen.py
├── requirements.txt
└── README.md
```

## Ethical Disclaimer

This project is intended for educational and authorized personal use only. The author is not responsible for any misuse of this tool. Use a password manager to store generated passwords securely.
```

---
