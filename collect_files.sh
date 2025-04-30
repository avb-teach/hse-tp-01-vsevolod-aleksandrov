#!/bin/bash

if [[ $# -lt 2 ]]; then
    echo "Использование: $0 <входная_директория> <выходная_директория> [--max_depth N]"
    exit 1
fi

python3 collect_files.py "$@"
