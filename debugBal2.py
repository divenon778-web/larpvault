import re
b=r'C:\Users\micha\Downloads\saveweb2zip-com-rbxvault-co'
p=b+'\\js\\layout-b16629b22e77896b.js'
# Read raw bytes
with open(p, 'rb') as f:
    raw = f.read()

# Find the exact bytes at the position
# The character is at position around 9087 in the decoded string
# Let's find the exact bytes
idx = raw.find(b'customerBalanceCents')
if idx >= 0:
    # Print bytes around this position
    start = max(0, idx - 100)
    end = min(len(raw), idx + 200)
    print('raw bytes:', raw[start:end])
    print()
    # Decode to see
    print('decoded:', raw[start:end].decode('utf-8', errors='replace'))

# Also find the actual balance display
# Search for the pattern with the dash
balance_pattern = b'null!=(t=L.customerBalanceCents)'
idx2 = raw.find(balance_pattern)
if idx2 >= 0:
    s = max(0, idx2 - 50)
    e = min(len(raw), idx2 + 150)
    print('balance pattern:', raw[s:e])
    print('decoded:', raw[s:e].decode('utf-8', errors='replace'))