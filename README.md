# Seed Phrase Search Program

This project is a cross-platform Python utility designed to search for recovery seed phrases in text files. It is specifically intended to identify 12-word recovery seed phrases that are commonly used in cryptocurrency wallets, based on the [BIP39 standard](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki).

## Features
- **Cross-platform**: Works on Windows and macOS.
- **Seed Phrase Detection**: Searches for 12-word seed phrases based on the BIP39 wordlist.
- **Progress Bar**: Uses `tqdm` to provide a real-time progress bar during the search.
- **File Filtering**: Only processes text files, skipping binary and unreadable files.

## Requirements
- Python 3.6 or higher
- `tqdm` library for the progress bar

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/seed_phrase_search.git
   cd seed_phrase_search
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   The `requirements.txt` file should contain:
   ```
   tqdm
   ```

3. **Download BIP39 Wordlist**
   The program requires a file named `bip39_wordlist.txt` containing the 2048 words from the BIP39 standard. You can download this file from [the official GitHub repository](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt) or create it manually.

## Usage
Run the program from the command line with the path to the directory you want to search:
```bash
python seed_phrase_search.py <path_to_directory>
```
Replace `<path_to_directory>` with the path of the folder you want to search.

For example:
```bash
python seed_phrase_search.py C:\Users\YourName\Documents
```

## BIP39 Wordlist
The file `bip39_wordlist.txt` is a text file containing all 2048 words defined by the BIP39 standard, each word on a separate line. This list is used by the program to identify potential 12-word seed phrases in files.

**Note**: Ensure that the `bip39_wordlist.txt` file is in the same directory as `seed_phrase_search.py` or provide the correct path to it in the script.

## How It Works
1. **Input Path**: The user provides a file path to search.
2. **Text File Filtering**: The program checks if each file is a text file before searching.
3. **Seed Phrase Detection**: Files are scanned for sequences of 12 words that match words from the BIP39 wordlist.
4. **Progress Bar**: A progress bar is shown during the search to indicate how many files have been processed.

## Example Output
```
[FOUND] Seed phrase in: C:\Users\YourName\Documents\example.txt
```
The program will print the path of any files containing a 12-word recovery seed phrase.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributions
Contributions are welcome! Feel free to open issues or pull requests.

## Disclaimer
This tool is provided for educational purposes only. Use responsibly and respect privacy when using this tool to avoid unauthorized access to sensitive data.


