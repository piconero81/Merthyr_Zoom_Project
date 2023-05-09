import os
import time
import sys
import subprocess

os.chdir(r"C:\Users\wanka\Documents\OnlyM\Media")
all_files = os.listdir()

for f in all_files:
    os.remove(f)

print(os.listdir())