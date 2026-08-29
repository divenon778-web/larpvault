$b='C:\Users\micha\Downloads\saveweb2zip-com-rbxvault-co'
foreach($p in @("$b\dashboard\index.html","$b\dashboard\market\index.html")){
  $h=Get-Content $p -Raw -Encoding UTF8
  $h=[regex]::Replace($h,'<script[^>]*src="[^"]*\.js"[^>]*></script>','')
  $h=[regex]::Replace($h,'<script>self\.__next_f[^<]*</script>','')
  Set-Content $p -Value $h -NoNewline -Encoding UTF8
  Write-Host "stripped $(Split-Path $p -Leaf) in $(Split-Path (Split-Path $p -Parent) -Leaf)"
}
Write-Host "dashboard static"
