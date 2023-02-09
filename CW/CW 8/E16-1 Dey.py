import re
ip = '216.09.084.01'
pattern = r'\.[0]*'
string = re.sub('\.[0]*', '.', ip)
print(string)