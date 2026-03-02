File Integrity Checker

A beginner-friendly Python tool that monitors file integrity by computing SHA-256 hashes, creating a baseline snapshot, and detecting unauthorized changes (modified, added, or deleted files). Built as a self-learning cybersecurity project in November 2025.

[Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
[License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

 Features

- Recursive directory scanning (`os.walk`)
- Efficient chunked hashing for large files (`hashlib.sha256`)
- Baseline hashes saved to JSON
- Interactive command-line interface (`create` / `verify`)
- Case-insensitive path handling (Windows-friendly)
- Basic error handling & user input validation

 Demo (Verification after changes)

Integrity issues found:
Modified: c:\users\abuvm\desktop\secure_files\notes.txt
New:      c:\users\abuvm\desktop\secure_files\new.txt
Missing:  c:\users\abuvm\desktop\secure_files\example.txt

Installation & Usage

Clone the repository:
git clone https://github.com/abbangural19-maker/file-integrity-checker.git
cd file-integrity-checker

Run the script:
python integrity_checker.py

Follow the prompts:
Enter the directory path to monitor
Choose create (generate baseline) or verify (check for changes)


Project Structure
file-integrity-checker/
├── integrity_checker.py       Main script
├── README.md                  This file
├── screenshots/               Visuals of code, outputs, tests
└── docs/                      Reflections, test notes, etc.

What I Learned

Practical application of cryptographic hashing for file integrity
File system traversal and JSON data persistence
Debugging path/case-sensitivity issues on Windows
Real-world connection to tools like Tripwire, AIDE, OSSEC
Importance of error handling and user-friendly CLI design

This project showed me how simple hashing can prevent big security issues (e.g., detecting ransomware modifications or tampering).

Screenshots
All test outputs, code views, and edge-case results are in the /screenshots/ folder.

Future Ideas

Add scheduled automatic checks (cron / Task Scheduler)
Email/SMS alerts on changes
Simple GUI with tkinter
Whitelist support to reduce false positives
