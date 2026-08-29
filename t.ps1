$b='C:\Users\micha\Downloads\saveweb2zip-com-rbxvault-co'
$f="$b\js\layout-b16629b22e77896b.js"
$c=Get-Content $f -Raw -Encoding UTF8
$c=$c.Replace('):"-"','):\"$0.00\"')
# Actually need to replace the string literal "-" with "$0.00" for the balance fallback
# The pattern is ):\"-\" at the end of the ternary
$c=$c.Replace('):"-"','') # placeholder
Set-Content $f -Value $c -NoNewline -Encoding UTF8
Write-Host "test"
