import re
b=r'C:\Users\micha\Downloads\saveweb2zip-com-rbxvault-co'
p=b+'\\js\\layout-b16629b22e77896b.js'
c=open(p,'r',encoding='utf-8').read()

# The issue is at the end: ):"�"}
# Find and replace the U+FFFD in the balance display
# Pattern: k("VENDOR"...):"�"}
# Replace the U+FFFD with $0.00

# The exact pattern is: ):"�"}
old = '):"\uFFFD"})'
new = '):"$0.00"})'
if old in c:
    c = c.replace(old, new)
    print('replaced specific pattern')
else:
    # Try with the actual char
    c = c.replace('\uFFFD', '$0.00')
    print('replaced all U+FFFD')

# Write back
with open('C:\\Users\\micha\\Downloads\\saveweb2zip-com-rbxvault-co\\js\\layout-b16629b22e77896b.js', 'w', encoding='utf-8') as f:
    f.write(c)

# Copy to _next
import shutil
shutil.copy('C:\\Users\\micha\\Downloads\\saveweb2zip-com-rbxvault-co\\js\\layout-b16629b22e77896b.js', 
            'C:\\Users\\micha\\Downloads\\saveweb2zip-com-rbxvault-co\\_next\\static\\chunks\\layout-b16629b22e77896b.js')
shutil.copy('C:\\Users\\micha\\Downloads\\saveweb2zip-com-rbxvault-co\\js\\layout-b16629b22e77896b.js', 
            'C:\\Users\\micha\\Downloads\\saveweb2zip-com-rbxvault-co\\_next\\static\\chunks\\app\\dashboard\\layout-b16629b22e77896b.js')
print('done - balance fixed to $0.00')