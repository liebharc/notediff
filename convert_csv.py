import json
import re

file_content = open('Ghostship.txt').readlines()
for line in file_content:
    match = re.search(r'INFO\s+(.*)$', line)
    if match:
        print(match.group(1).strip())