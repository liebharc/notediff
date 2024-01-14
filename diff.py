import sys
import re
import difflib

file_content = open(sys.argv[1]).readlines()

def norm_string(s: str):
    s = s.replace("r", "")
    s = re.sub(r'\d+', '', s).strip()
    return s.split(" ")

for line in file_content:
    parts = line.strip().split(",")
    reference = parts[0]
    actual = parts[1]
    reference = norm_string(reference)
    actual = norm_string(actual)
    print(reference, "vs", actual)