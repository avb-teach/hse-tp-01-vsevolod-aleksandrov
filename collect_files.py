import os
import sys
import shutil
from pathlib import Path

def process_files(input_dir, output_dir, max_depth=None, current_depth=0):
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    for entry in os.scandir(input_dir):
        if entry.is_file():
            file_name = entry.name
            dest_path = Path(output_dir) / file_name
            suffix = 1
            while dest_path.exists():
                base_name, ext = os.path.splitext(file_name)
                new_name = f"{base_name}_{suffix}{ext}"
                dest_path = Path(output_dir) / new_name
                suffix += 1
            try:
                shutil.copy(entry.path, dest_path)
            except Exception:
                pass
        elif entry.is_dir() and (max_depth is None or current_depth < max_depth):
            process_files(entry.path, output_dir, max_depth, current_depth + 1)

if len(sys.argv) < 3:
    print("Usage: python script.py input_dir output_dir [--max_depth N]")
    sys.exit(1)

input_dir = sys.argv[1]
output_dir = sys.argv[2]
max_depth = None

if "--max_depth" in sys.argv:
    try:
        max_depth_index = sys.argv.index("--max_depth")
        max_depth = int(sys.argv[max_depth_index + 1])
        if max_depth > 3:
            print("Error: --max_depth cannot be greater than 3.")
            sys.exit(1)
    except (ValueError, IndexError):
        print("Error: --max_depth must be an integer.")
        sys.exit(1)

process_files(input_dir, output_dir, max_depth)
