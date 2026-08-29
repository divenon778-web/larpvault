import re
b=r'C:\Users\micha\Downloads\saveweb2zip-com-rbxvault-co'
p=b+'\\js\\layout-b16629b22e77896b.js'
c=open(p,'r',encoding='utf-8').read()

# Count and show the ):"-" patterns
matches = list(re.finditer(r'\):\"-"', c))
print(f'found {len(matches)} instances of ):"-"')
for m in matches:
    s = max(0, m.start()-50)
    e = min(len(c), m.end()+50)
    print(f'  at {m.start()}: ...{c[s:m.end()+20]}...')

# Replace all ):"-" with ):"$0.00" (for balance displays)
c2 = c.replace('):"-"', '):"$0.00"')

# Write back
with open(p,'w',encoding='utf-8') as f:
    f.write(c.replace('):"-"', '):"$0.00"'))

# Copy to _next
import shutil
shutil.copy('C:\\Users\\micha\\Downloads\\saveweb2zip-com-rbxvault-co\\js\\layout-b16629b22e77896b.js', 
            'C:\\Users\\micha\\Downloads\\saveweb2zip-com-rbxvault-co\\_next\\static\\chunks\\layout-b16629b22e77896b.js')
shutil.copy('C:\\Users\\micha\\Downloads\\saveweb2zip-com-rbxvault-co\\js\\layout-b16629b22e77896b.js', 
            'C:\\Users\\micha\\Downloads\\saveweb2zip-com-rbxvault-co\\_next\\static\\chunks\\app\\dashboard\\layout-b16629b22e77896b.js')
print("done - all ):\"-\" replaced")