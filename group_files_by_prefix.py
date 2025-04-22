#!/usr/bin/env python3

import os
import shutil
import sys

def group_files_by_prefix(folder_path):
    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a valid directory.")
        sys.exit(1)

    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)

        # Only process files
        if not os.path.isfile(full_path):
            continue

        # Split at " - " and get the prefix
        if " - " in filename:
            prefix = filename.split(" - ")[0]
            target_dir = os.path.join(folder_path, prefix)

            # Create the target directory if it doesn't exist
            os.makedirs(target_dir, exist_ok=True)

            # Move the file
            target_path = os.path.join(target_dir, filename)
            print(f"Moving: {filename} -> {target_dir}/")
            shutil.move(full_path, target_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 group_files.py <folder_path>")
        sys.exit(1)

    folder = sys.argv[1]
    group_files_by_prefix(folder)
