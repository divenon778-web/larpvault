import re
b=r'C:\Users\micha\Downloads\saveweb2zip-com-rbxvault-co'
p=b+'\\js\\layout-b16629b22e77896b.js'
c=open(p,'r',encoding='utf-8').read()

# Find the exact character at the problematic position
# The issue is at position around 9087
pos = 9087
print('char at 9087:', repr(c[9087]), 'code:', ord(c[9087]) if 9087 < len(c) else 'OOB')
print('context:', repr(c[9080:9100]))

# Also check the actual char at the end of the balance ternary
# The pattern is at the end of the ternary expression
# Find the pattern with the replacement char
for m in re.finditer(r'[^\\w\s]{1}', c):
    ch = m.group()
    if ord(ch) >= 0xFF00 or ch == '\uFFFD':
        print('non-ascii at', m.start(), ':', repr(ch), ord(ch))
        
# Also try to find the specific balance display
# The balance is shown in a span with the formatted value
# Look for the span that shows the balance
# It's likely in the layout where B is displayed
for m in re.finditer(r'B', c):
    if m.start() > 9000 and m.start() < 9200:
        print('B at', m.start(), 'context:', c[m.start()-60:m.end()+60])
        break