import re

match = re.finditer(r'([0-9]{1,3})', 'Exercises number 1, 12, 123 are important')
for m in match:
    print(m.group())
# import re
# def match(text):
#     pattern = r'[0-9]{1,3}\b'                   #[0-9]$
#     if re.finditer(pattern, text):
#         return 'a match found'
#     else:
#         return 'not match'
# print(match('The quick 1234 brown fox jumps over the lazy dog'))
# print(match('ahra32'))
# print(match('abcdef'))
# print(match('abcdef90'))