import re

pattern=r'\d+'
text = "there are 123 apple 456"
match = re.search(pattern,text)
print(match.group())
