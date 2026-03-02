import hashlib
import os
import json

def compute_hash(file_path):
    """Compute SHA-256 hash of a file."""
    sha256 = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(4096):  # Read in chunks to handle large files
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception as e:
        print(f"Error hashing {file_path}: {e}")
        return None

def create_baseline(directory, baseline_file='baseline.json'):
    """Scan directory and save file hashes to baseline JSON."""
    hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file).lower()  # Normalize to lowercase
            hash_value = compute_hash(file_path)
            if hash_value:
                hashes[file_path] = hash_value
    with open(baseline_file, 'w') as f:
        json.dump(hashes, f, indent=4)
    print(f"Baseline created and saved to {baseline_file}")

def verify_integrity(directory, baseline_file='baseline.json'):
    """Re-scan directory and compare hashes to baseline."""
    try:
        with open(baseline_file, 'r') as f:
            baseline_hashes = {k.lower(): v for k, v in json.load(f).items()}  # Normalize keys
    except FileNotFoundError:
        print("Baseline file not found. Create one first.")
        return
    except Exception as e:
        print(f"Error loading baseline: {e}")
        return

    current_hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file).lower()  # Normalize to lowercase
            hash_value = compute_hash(file_path)
            if hash_value:
                current_hashes[file_path] = hash_value

    # Compare
    issues = []
    for file_path, baseline_hash in baseline_hashes.items():
        if file_path not in current_hashes:
            issues.append(f"Missing: {file_path}")
        elif current_hashes[file_path] != baseline_hash:
            issues.append(f"Modified: {file_path}")

    for file_path in current_hashes:
        if file_path not in baseline_hashes:
            issues.append(f"New: {file_path}")

    if issues:
        print("Integrity issues found:")
        for issue in issues:
            print(issue)
    else:
        print("All files match the baseline. No changes detected.")

if __name__ == "__main__":
    try:
        directory = input("Enter directory path to monitor: ").strip()
        if not os.path.isdir(directory):
            raise ValueError("Invalid directory path. Please enter a valid folder.")
       
        action = input("Enter 'create' to make baseline or 'verify' to check: ").lower().strip()
       
        if action == 'create':
            create_baseline(directory)
        elif action == 'verify':
            verify_integrity(directory)
        else:
            raise ValueError("Invalid action. Choose 'create' or 'verify'.")
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")