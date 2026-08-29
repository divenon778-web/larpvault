import re
b=r'C:\Users\micha\Downloads\saveweb2zip-com-rbxvault-co'
p=b+'\\js\\layout-b16629b22e77896b.js'
c=open(p,'r',encoding='utf-8').read()

# Fix the balance display: replace the � (U+FFFD) with $0.00
# The pattern is: k(B):"loading"!==L.id?k("VENDOR"===L.currentMode?null!=(e=L.vendorBalanceCents)?e:0:null!=(t=L.customerBalanceCents)?t:0):"�"
# Replace the � with $0.00

# Replace the specific pattern
old = 'null!=(t=L.customerBalanceCents)?t:0):"\uFFFD"'
new = 'null!=(t=L.customerBalanceCents)?t:0):"$0.00"'
if old in c:
    c = c.replace(old, new)
    print('replaced specific pattern')
else:
    print('pattern not found exactly, trying alternatives...')
    # Try with the actual replacement char
    c2 = c.replace('\uFFFD', '$0.00')
    if c2 != c:
        c = c2
        print('replaced all U+FFFD')
    else:
        # Try with the actual char
        c2 = c.replace('�', '$0.00')
        if c2 != c:
            c = c2
            print('replaced � char')
        else:
            # Try regex
            c2 = re.sub(r'([\uFFFD])', '$0.00', c)
            if c2 != c:
                c = c2
                print('replaced via regex')
            else:
                print('nothing worked')

# Write back
with open('C:\\Users\\micha\\Downloads\\saveweb2zip-com-rbxvault-co\\js\\layout-b16629b22e77896b.js', 'w', encoding='utf-8') as f:
    f.write(c)
print('written')

# Copy to _next
import shutil
shutil.copy('C:\\Users\\micha\\Downloads\\saveweb2zip-com-rbxvault-co\\js\\layout-b16629b22e77896b.js', 
            'C:\\Users\\micha\\Downloads\\saveweb2zip-com-rbxvault-co\\_next\\static\\chunks\\layout-b16629b22e77896b.js')
shutil.copy('C:\\Users\\micha\\Downloads\\saveweb2zip-com-rbxvault-co\\js\\layout-b16629b22e77896b.js', 
            'C:\\Users\\micha\\Downloads\\saveweb2zip-com-rbxvault-co\\_next\\static\\chunks\\app\\dashboard\\layout-b16629b22e77896b.js')
print('copied to _next')