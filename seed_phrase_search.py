import os
import re
import argparse
from pathlib import Path
from tqdm import tqdm
import mimetypes

# Load the BIP39 wordlist
BIP39_WORDLIST_PATH = "bip39_wordlist.txt"
with open(BIP39_WORDLIST_PATH, 'r') as f:
    BIP39_WORDLIST = set(word.strip() for word in f.readlines())

# Function to check if a file contains a 12-word recovery phrase
def contains_seed_phrase(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            
            # Sliding window of 12 words to check if all words are in BIP39 wordlist
            for i in range(len(words) - 11):
                if all(word in BIP39_WORDLIST for word in words[i:i+12]):
                    return True
    except (UnicodeDecodeError, PermissionError, FileNotFoundError):
        # Skip files that can't be read
        pass
    return False

# Function to check if a file is a text file
def is_text_file(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type is not None and mime_type.startswith('text')

# Recursive function to search for seed phrases in files under a given path
def search_files(base_path):
    base_path = Path(base_path)
    if not base_path.exists():
        print(f"Error: The path {base_path} does not exist.")
        return

    # Get the list of all files to be processed
    all_files = [Path(root) / file for root, _, files in os.walk(base_path) for file in files]
    total_files = len(all_files)

    # Progress bar setup
    with tqdm(total=total_files, unit='file', desc='Searching files') as pbar:
        for file_path in all_files:
            if is_text_file(file_path) and contains_seed_phrase(file_path):
                print(f"[FOUND] Seed phrase in: {file_path}")
            pbar.update(1)

# Main function to parse arguments and start the search
def main():
    parser = argparse.ArgumentParser(description="Search for crypto wallet recovery seed phrases in files.")
    parser.add_argument('path', type=str, help='The base path to start searching from')
    args = parser.parse_args()

    search_files(args.path)

if __name__ == "__main__":
    main()
