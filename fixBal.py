b=r'C:\Users\micha\Downloads\saveweb2zip-com-rbxvault-co'
p=b+'\\js\\layout-b16629b22e77896b.js'
c=open(p,'r',encoding='utf-8').read()
# Fix balance fallback from "-" to "$0.00"
# The pattern is ):\"-\" at end of balance ternary
c=c.replace('):"-"','):\"$0.00\"')
# More specific for the balance fallback
old='null!=(t=L.customerBalanceCents)?t:0):"-"'
new='null!=(t=L.customerBalanceCents)?t:0):"$0.00"'
if old in c:
    c=c.replace(old,new)
    print("replaced specific")
else:
    print("not found specific, trying generic")
    # Generic: find the last occurrence of :"-" near balance
    import re
    c=re.sub(r'\)\:"-"', '):"$0.00"', c)
open(p,'w',encoding='utf-8').write(c)
# Copy to _next
import shutil
shutil.copy(p, b+'\\_next\\static\\chunks\\layout-b16629b22e77896b.js')
shutil.copy(p, b+'\\_next\\static\\chunks\\app\\dashboard\\layout-b16629b22e77896b.js')
print("done")
