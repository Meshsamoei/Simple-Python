import sys
from sys import argv
import os
import time
from pathlib import Path

is_path = argv[1]


for file in os.listdir(is_path):
    file_path = os.path.abspath(file)
    if file.endswith(".mp3"):
        print(f"", file)
    print(f"File >", file, "Path >" ,file_path)
    print()