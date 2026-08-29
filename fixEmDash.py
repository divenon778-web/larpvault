import re
b=r'C:\Users\micha\Downloads\saveweb2zip-com-rbxvault-co'
p=b+'\\js\\layout-b16629b22e77896b.js'

# Read raw bytes and replace the EM DASH (U+2014, bytes \xe2\x80\x94) with $0.00 for balance
with open(p, 'rb') as f:
    raw = f.read()

# Replace the em dash (U+2014, bytes \xe2\x80\x94) with $0.00 for balance
# The em dash is \xe2\x80\x94 in UTF-8
raw = raw.replace(b'\xe2\x80\x94', b'$0.00')

# Also fix the username fallback - it should show @larp not the em dash
# The username fallback is already fixed to @larp in the JS, but let's make sure
# Also need to fix the balance display specifically

# Write back
with open('C:\\Users\\micha\\Downloads\\saveweb2zip-com-rbxvault-co\\js\\layout-b16629b22e77896b.js', 'wb') as f:
    f.write(raw)

# Copy to _next
import shutil
shutil.copy('C:\\Users\\micha\\Downloads\\saveweb2zip-com-rbxvault-co\\js\\layout-b16629b22e77896b.js', 
            'C:\\Users\\micha\\Downloads\\saveweb2zip-com-rbxvault-co\\_next\\static\\chunks\\layout-b16629b22e77896b.js')
shutil.copy('C:\\Users\\micha\\Downloads\\saveweb2zip-com-rbxvault-co\\js\\layout-b16629b22e77896b.js', 
            'C:\\Users\\micha\\Downloads\\saveweb2zip-com-rbxvault-co\\_next\\static\\chunks\\app\\dashboard\\layout-b16629b22e77896b.js')
print('replaced EM DASH (U+2014) with $0.00 for balance')