import re
b=r'C:\Users\micha\Downloads\saveweb2zip-com-rbxvault-co'
p=b+'\\js\\layout-b16629b22e77896b.js'
c=open(p,'r',encoding='utf-8').read()

# Find the exact character at the end of the balance display
# The pattern is at position ~9014
pos = 9014
print('char at 9014:', repr(c[9014]), 'code:', ord(c[9014]))
print('context:', repr(c[9010:9020]))

# Find the exact characters around the replacement
# The pattern is at the end of the ternary: ):"�"}
# Let's find it exactly
idx = c.find('):"')
while idx != -1:
    if idx > 9000 and idx < 9100:
        print('found at', idx, ':', repr(c[idx:idx+10]))
    idx = c.find('):"', idx+1)

# Check what the actual character is
for i in range(9010, 9020):
    ch = c[i]
    print(f'{i}: {repr(c[i])} code={ord(c[i])}')