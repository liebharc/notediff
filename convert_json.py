import json
import re

file_content = open('God Rest Ye Merry Gentlemen.txt').read()
json_content = json.loads(file_content)
for line in json_content:
    match = re.search(r'INFO\s+(.*)$', line["message"])
    if match:
        print(match.group(1).strip())