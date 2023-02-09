import re
pattern = ['red', 'brown', 'yellow']
text = 'the quick yellow fox jumps over the dog'
for i in pattern:
    print(f'searching for {i} in {text}')
    if re.search(i, text):
        print('Matched')
    else:
        print('Not matched')
