import re

# this captures sequences of alphabetic characters
# possibily followed by an apostrophe and more characters
# n.b. (?:...) denotes a non-capturing group
def simple_tokenize(s):
    return re.findall(r"[a-z]+(?:'[a-z]+)?",s.lower())
