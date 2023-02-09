import re
text = 'the quick brown fox jumps over the lazy dog'
pattern = 'fox'
match = re.search(pattern, text)
s = match.start()
e = match.end()
print(f'found {match.re.pattern} in {match.string} from {s}, {e}')
