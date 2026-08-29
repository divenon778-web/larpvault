import re
b=r'C:\Users\micha\Downloads\saveweb2zip-com-rbxvault-co'
p=b+'\\js\\layout-b16629b22e77896b.js'
c=open(p,'r',encoding='utf-8').read()

# Find the exact replacement char position
# The issue is at: ):"�"}) at the end of the ternary
# Let's find and replace the U+FFFD character
count_before = c.count('\uFFFD')
print('U+FFFD count:', count_before)

# Replace all U+FFFD with $0.00
c = c.replace('\uFFFD', '$0.00')

# Also check if there's a different encoding issue - maybe the file has the literal bytes
# Write back
with open('C:\\Users\\micha\\Downloads\\saveweb2zip-com-rbxvault-co\\js\\layout-b16629b22e77896b.js', 'w', encoding='utf-8') as f:
    f.write(c)

# Copy to _next
import shutil
shutil.copy('C:\\Users\\micha\\Downloads\\saveweb2zip-com-rbxvault-co\\js\\layout-b16629b22e77896b.js', 
            'C:\\Users\\micha\\Downloads\\saveweb2zip-com-rbxvault-co\\_next\\static\\chunks\\layout-b16629b22e77896b.js')
shutil.copy('C:\\Users\\micha\\Downloads\\saveweb2zip-com-rbxvault-co\\js\\layout-b16629b22e77896b.js', 
            'C:\\Users\\micha\\Downloads\\saveweb2zip-com-rbxvault-co\\_next\\static\\chunks\\app\\dashboard\\layout-b16629b22e77896b.js')
print('done - replaced U+FFFD with $0.00')