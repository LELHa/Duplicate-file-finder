# Duplicate File Finder

A Python tool designed to detect duplicate files in a directory using file hashes.

The goal of this project is to analyze a file system, identify files with exactly the same content, and estimate the disk space that can be recovered by removing unnecessary copies.

---

## Features

- Recursive directory scanning
- File discovery and analysis
- Exclusion of unnecessary folders (`.venv`, `.git`, `__pycache__`)
- SHA-256 hash calculation
- Duplicate file detection
- File grouping based on hash values
- Recoverable disk space calculation
- Human-readable file size conversion
- Command-line usage

---

## How It Works

### File Scanning

The first step is to scan a selected directory and retrieve all existing files.

The program recursively explores the directory and its subdirectories using Python's `pathlib` module.

The scanner collects all files that need to be analyzed while ignoring unnecessary folders such as virtual environments and Git metadata.

---

### File Hashing

To identify identical files, the program does not compare the entire content directly.

Instead, it calculates a unique fingerprint called a hash.

A hash is a fixed-size value generated from the content of a file. Two files with exactly the same content will produce the same hash value.

The project uses the SHA-256 algorithm to generate file fingerprints.

---

## Why SHA-256?

Several hashing algorithms exist, such as MD5, SHA-256, and SHA-512.

MD5 was not chosen because it is vulnerable to collision issues. A collision occurs when two different files generate the same hash value, which could lead to incorrect duplicate detection.

SHA-256 was chosen because it provides a strong balance between reliability and performance.

SHA-512 offers a longer hash and an even lower probability of collisions, but it requires more computation. For this project, SHA-256 is fast enough while providing sufficient accuracy for duplicate detection.

---

## Duplicate Detection

After calculating the hash of each file, the program groups files using their hash value.

A dictionary is used to associate each hash with the list of files having the same content.

Files belonging to a group containing multiple entries are considered duplicates.

---

## Recoverable Disk Space

The tool calculates how much storage space can be recovered by removing duplicate copies.

For each duplicate group, the program keeps one file and calculates the space occupied by the unnecessary copies.

---

## File Size Formatting

File sizes are initially retrieved in bytes.

The program converts these values into human-readable units such as KB, MB, and GB to make the results easier to understand.

---

# Installation
copy the repository then write the : 
'''bash
python main.py

Select the directory to analyze and the program will scan the files, calculate their hashes, detect duplicates, and display the recoverable space.
