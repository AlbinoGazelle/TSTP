import re

""" l = "Beautiful is better than ugly"

matches = re.findall("Beautiful", l, re.IGNORECASE)

print(matches) """

line = "123?34 hello?"

m = re.findall("\d", line, re.IGNORECASE)

print(m)