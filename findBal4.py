import re
b=r'C:\Users\micha\Downloads\saveweb2zip-com-rbxvault-co'
p=b+'\\js\\layout-b16629b22e77896b.js'
c=open(p,'r',encoding='utf-8').read()

# Find the balance display - look for the pattern with balance
# The balance is shown with k(B) or similar
# Search for the string "balance" or "Balance" in the file
matches = list(re.finditer(r'B[^a-zA-Z]', c))
print('B patterns:', len([m for m in matches]))
for m in list(re.finditer(r'B', c))[:10]:
    s = max(0, m.start()-60)
    print('B at', m.start(), ':', c[max(0,m.start()-80):m.end()+80])
    print()

# Also look for customerBalanceCents
for m in re.finditer(r'customerBalanceCents', c):
    s = max(0, m.start()-100)
    print('customerBalanceCents at', m.start(), ':', c[m.start()-100:m.end()+80])
    print()