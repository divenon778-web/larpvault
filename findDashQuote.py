import re
b=r'C:\Users\micha\Downloads\saveweb2zip-com-rbxvault-co'
p=b+'\\js\\layout-b16629b22e77896b.js'
c=open(p,'r',encoding='utf-8').read()

# Find all quote-dash-quote patterns
matches = list(re.finditer(r'[\"\']-[\"\']', c))
print('found', len(matches), 'quote-dash-quote patterns')
for m in matches:
    s = max(0, m.start()-60)
    e = min(len(c), m.end()+60)
    print('  at', m.start(), ':', c[s:m.end()+80])
    print()