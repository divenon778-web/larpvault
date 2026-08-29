import re
b=r'C:\Users\micha\Downloads\saveweb2zip-com-rbxvault-co'
p=b+'\\js\\layout-b16629b22e77896b.js'
c=open(p,'r',encoding='utf-8').read()

# Find all } after the balance ternary
for i in range(len(c)):
    if c[i] == '}' and i > 9000 and i < 9500:
        ctx = c[max(0,i-40):i+10]
        if '\uFFFD' in ctx or '�' in ctx:
            print(f'found at {i}: {repr(ctx)}')
            break

# Also check for the actual character in the file
print('Total U+FFFD in file:', c.count('\uFFFD'))

# Let's also check the raw bytes for the actual character
with open('C:\\Users\\micha\\Downloads\\saveweb2zip-com-rbxvault-co\\js\\layout-b16629b22e77896b.js', 'rb') as f:
    raw = f.read()

# Find the actual bytes at the end of the balance display
idx = raw.find(b':"')
while idx != -1:
    if idx > 8000 and idx < 9500:
        print(f'found at {idx}: {raw[idx:idx+20]}')
    idx = raw.find(b':"', idx+1)