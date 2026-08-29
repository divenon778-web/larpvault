b=r'C:\Users\micha\Downloads\saveweb2zip-com-rbxvault-co'
p=b+'\\js\\layout-b16629b22e77896b.js'
c=open(p,'r',encoding='utf-8').read()

# Find the balance display - look for where k(B) or balance is rendered
import re
for m in re.finditer(r'k\([^)]*\)', c):
    s = max(0, m.start()-50)
    e = min(len(c), m.end()+80)
    print('at', m.start(), ':', c[s:m.end()+80])
    print()