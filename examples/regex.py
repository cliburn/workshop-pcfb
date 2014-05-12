import re

find = r'(\d+)\s+(\w{3})[\w\,\.]*\s+(\d+)\sat\s(\d+):(\d+)\s+([-\d\.]+)\s+([-\d\.]+).*'
replace = r'\3\t\2.\t\1\t\4\t\5\t\6\t\7'

for line in open('examples/Ch3observations.txt'):
    newline = re.sub(find, replace, line)
    print newline,
