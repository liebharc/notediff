import sys
import re
import difflib

file_content = open(sys.argv[1]).readlines()

def norm_string(s: str):
    s = s.replace("r", "")
    s = re.sub(r'\d+', '', s).strip()
    return s.split(" ")

def diff(a, b):
    return difflib.SequenceMatcher(None, a, b).get_matching_blocks()

for line in file_content:
    parts = line.strip().split(",")
    reference = parts[0]
    actual = parts[1]
    reference = norm_string(reference)
    actual = norm_string(actual)
    print(str.join("", reference), "vs", str.join("", actual), diff(reference, actual))