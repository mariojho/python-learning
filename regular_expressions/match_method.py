# Regular expressions - match method

import re
regex = re.compile('([0-9]+)\.([0-9]+)')
MATCH = regex.search("pi: 3.1415926535897931")
print(MATCH.group(0))
print(MATCH.group(1))
print(MATCH.group(2))

print(MATCH.start())

print(MATCH.end())