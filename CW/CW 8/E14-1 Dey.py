import re
def match(text):
    pattern = r'^[A-Za-z0-9_]*$'    #\w*z.\w*
    if re.findall(pattern, text):
        return 'a match found'
    else:
        return 'not match'
print(match('The quick brown fox jumps over the lazy dog'))
print(match('Zahra_rezaei2'))