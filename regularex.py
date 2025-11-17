# regular expressions in Python
import re
pattern = r"\bfoo\b"
text = "foo bar foobar foo"
matches = re.findall(pattern, text)
print(matches)

# re.search example
search_result = re.search(r"bar", text)
if search_result:
    print("Found 'bar' in text at position:", search_result.start())

# re.search index example
import re

s = 'GeeksforGeeks: A computer science portal for geeks'
match = re.search(r'portal', s)

print('Start Index:', match.start())
print('End Index:', match.end())