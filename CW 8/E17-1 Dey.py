import re
def match(text):
    pattern = r'.*[0-9]$'                   #[0-9]$
    if re.findall(pattern, text):
        return 'a match found'
    else:
        return 'not match'
print(match('The quick brown fox jumps over the lazy dog'))
print(match('ahra32'))
print(match('abcdef'))
print(match('abcdef90'))