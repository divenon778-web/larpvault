$b='C:\Users\micha\Downloads\saveweb2zip-com-rbxvault-co'
foreach($p in @("$b\dashboard\index.html","$b\dashboard\market\index.html")){
  $h=Get-Content $p -Raw -Encoding UTF8
  # Remove ALL script tags that have src attribute
  $h=[regex]::Replace($h,'<script[^>]*src=[^>]*></script>','', [System.Text.RegularExpressions.RegexOptions]::IgnoreCase)
  # Remove ALL inline script tags that contain self.__next_f
  $h=[regex]::Replace($h,'<script[^>]*>self\.__next_f[^<]*</script>','', [System.Text.RegularExpressions.RegexOptions]::IgnoreCase)
  # Remove script tags with id _R_
  $h=[regex]::Replace($h,'<script[^>]*id="_R_"[^>]*></script>','', [System.Text.RegularExpressions.RegexOptions]::IgnoreCase)
  # Remove any script tag containing __next_f.push
  $h=[regex]::Replace($h,'<script[^>]*>.*__next_f\.push.*</script>','', [System.Text.RegularExpressions.RegexOptions]::Singleline)
  # Remove any remaining self.__next_f
  $h=[regex]::Replace($h,'<script[^>]*>.*self\.__next_f.*</script>','', [System.Text.RegularExpressions.RegexOptions]::Singleline)
  # Remove the initial script tag that redirects file://
  $h=$h.Replace('<script>if(location.protocol==="file:"){window.location="http://localhost:8787";}</script>','')
  # Ensure the guard script for auth is still there
  if(-not ($h -match 'larp_auth')){
    $h=$h.Replace('<head>','<head><script>if(!localStorage.getItem("larp_auth")){location.href="/login/";}</script>')
  }
  Set-Content $p -Value $h -NoNewline -Encoding UTF8
  Write-Host "stripped $(Split-Path $p -Leaf)"
}
Write-Host "dashboard fully static"